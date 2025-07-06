from telegram import Update
from telegram.ext import ContextTypes
from services.theme import ThemeService
from services.audio import AudioService

# /theme выбор
async def set_theme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await ThemeService.choose_theme(update, context)

# /settings (расширенная)
async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await ThemeService.settings_menu(update, context)

# Аудио выбор
async def choose_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await AudioService.choose_audio(update, context)
