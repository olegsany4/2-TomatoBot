from telegram import Update
from telegram.ext import ContextTypes
from services.timer import PomodoroTimer

# Команда /start
async def start_pomodoro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await PomodoroTimer.start(update, context)

# Команда /pause
async def pause_pomodoro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await PomodoroTimer.pause(update, context)

# Команда /skipbreak
async def skip_break(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await PomodoroTimer.skip_break(update, context)

# Команда /settings
async def show_settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await PomodoroTimer.show_settings(update, context)
