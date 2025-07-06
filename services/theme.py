class ThemeService:
    @staticmethod
    async def choose_theme(update, context):
        await update.message.reply_text("Выберите тему: light, dark, forest (заглушка)")

    @staticmethod
    async def settings_menu(update, context):
        await update.message.reply_text("Настройки таймера и темы (заглушка)")
