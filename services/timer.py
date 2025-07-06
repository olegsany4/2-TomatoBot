from telegram import Update
from telegram.ext import ContextTypes
from db.models import User, TimerSession
from db.session import async_session
from utils.scheduler import schedule_pomodoro, cancel_pomodoro
from datetime import datetime, timedelta

DEFAULT_POMODORO = 25 * 60
DEFAULT_SHORT_BREAK = 5 * 60
DEFAULT_LONG_BREAK = 15 * 60

class PomodoroTimer:
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        async with async_session() as session:
            user = await User.get_or_create(session, user_id)
            # Запуск новой сессии
            session_obj = TimerSession(
                user_id=user_id,
                start_time=datetime.utcnow(),
                end_time=datetime.utcnow() + timedelta(seconds=user.current_timer_settings.get('pomodoro', DEFAULT_POMODORO)),
                type='pomodoro',
            )
            session.add(session_obj)
            await session.commit()
        await update.message.reply_text("🍅 Pomodoro начат! 25 минут фокуса.")
        await schedule_pomodoro(context, user_id, session_obj.end_time, 'break')

    @staticmethod
    async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        await cancel_pomodoro(context, user_id)
        await update.message.reply_text("⏸️ Помидор на паузе.")

    @staticmethod
    async def skip_break(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        await cancel_pomodoro(context, user_id)
        await update.message.reply_text("⏭️ Отдых пропущен. Можно продолжать!")

    @staticmethod
    async def show_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        async with async_session() as session:
            user = await User.get_or_create(session, user_id)
            settings = user.current_timer_settings
        await update.message.reply_text(
            f"Текущие настройки:\n"
            f"Помидор: {settings.get('pomodoro', 25)} мин\n"
            f"Короткий отдых: {settings.get('short_break', 5)} мин\n"
            f"Длинный отдых: {settings.get('long_break', 15)} мин"
        )
