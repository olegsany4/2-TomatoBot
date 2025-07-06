from telegram import Update
from telegram.ext import ContextTypes

# /dailyreminder on|off HH:MM
async def daily_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ежедневное напоминание (заглушка)")
