from telegram import Update
from telegram.ext import ContextTypes
from db.models import Group, GroupMember
from db.session import async_session

# /creategroup Название
async def create_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите название группы: /creategroup Название")
        return
    name = ' '.join(context.args)
    async with async_session() as session:
        group = Group(name=name, is_public=False)
        session.add(group)
        await session.commit()
    await update.message.reply_text(f"Группа '{name}' создана!")

# /joingroup Код
async def join_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите код группы: /joingroup Код")
        return
    code = context.args[0]
    user_id = update.effective_user.id
    async with async_session() as session:
        group = await Group.get_by_code(session, code)
        if not group:
            await update.message.reply_text("Группа не найдена!")
            return
        member = GroupMember(user_id=user_id, group_id=group.group_id)
        session.add(member)
        await session.commit()
    await update.message.reply_text(f"Вы вступили в группу '{group.name}'!")

# /groupstats
async def group_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # MVP: просто stub
    await update.message.reply_text("Групповая статистика в разработке!")

# /leaderboard
async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Топ-10 по XP в разработке!")
