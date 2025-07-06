from telegram import Update
from telegram.ext import ContextTypes
from services.forest import ForestService
from db.session import async_session

# /forest - показать лес пользователя
async def show_forest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with async_session() as session:
        forest = await ForestService.get_forest(session, user_id)
    await update.message.reply_text(f"Ваш лес: {forest}")

# /stats - персональная статистика
async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with async_session() as session:
        stats = await ForestService.get_stats(session, user_id)
    await update.message.reply_text(stats)
