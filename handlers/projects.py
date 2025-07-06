from telegram import Update
from telegram.ext import ContextTypes
from db.models import Project
from db.session import async_session

# /projects - список проектов
async def list_projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with async_session() as session:
        projects = await Project.get_user_projects(session, user_id)
        if not projects:
            await update.message.reply_text("Нет проектов. Создайте через /newproject!")
            return
        msg = '\n'.join([f"- {p.name}" for p in projects])
        await update.message.reply_text(f"Ваши проекты:\n{msg}")
