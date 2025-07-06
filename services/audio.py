class AudioService:
    @staticmethod
    async def choose_audio(update, context):
        await update.message.reply_text("Выберите рингтон (заглушка)")
