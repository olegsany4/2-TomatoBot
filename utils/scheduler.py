from datetime import datetime
from telegram.ext import ContextTypes

# Простейший планировщик для Pomodoro (заглушка)
async def schedule_pomodoro(context: ContextTypes.DEFAULT_TYPE, user_id: int, end_time: datetime, next_phase: str):
    # Здесь будет интеграция с JobQueue
    pass

async def cancel_pomodoro(context: ContextTypes.DEFAULT_TYPE, user_id: int):
    # Здесь будет отмена JobQueue
    pass
