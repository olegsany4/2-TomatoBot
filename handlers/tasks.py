from telegram import Update
from telegram.ext import ContextTypes
from services.timer import PomodoroTimer
from db.models import Project, Task
from db.session import async_session
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# /newproject Название
async def new_project(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Укажите название проекта: /newproject Название")
        return
    name = ' '.join(context.args)
    user_id = update.effective_user.id
    async with async_session() as session:
        project = Project(user_id=user_id, name=name)
        session.add(project)
        await session.commit()
    await update.message.reply_text(f"Проект '{name}' создан!")

# /newtask [проект] Заголовок
async def new_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("/newtask [проект] Заголовок задачи")
        return
    user_id = update.effective_user.id
    async with async_session() as session:
        projects = await Project.get_user_projects(session, user_id)
        if len(projects) == 0:
            await update.message.reply_text("Сначала создайте проект через /newproject!")
            return
        if len(context.args) > 1 and any(p.name == context.args[0] for p in projects):
            project_name = context.args[0]
            title = ' '.join(context.args[1:])
            project = next(p for p in projects if p.name == project_name)
        else:
            project = projects[0]
            title = ' '.join(context.args)
        task = Task(project_id=project.project_id, title=title, status='active')
        session.add(task)
        await session.commit()
    await update.message.reply_text(f"Задача '{title}' добавлена в проект '{project.name}'!")

# /focus - выбрать задачу
async def focus_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with async_session() as session:
        tasks = await Task.get_active_tasks(session, user_id)
        if not tasks:
            await update.message.reply_text("Нет активных задач!")
            return
        keyboard = [[InlineKeyboardButton(t.title, callback_data=f"focus_{t.task_id}")] for t in tasks]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Выберите задачу для фокуса:", reply_markup=reply_markup)

# /done - завершить задачу
async def done_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with async_session() as session:
        task = await Task.get_focused_task(session, user_id)
        if not task:
            await update.message.reply_text("Нет выбранной задачи!")
            return
        task.status = 'done'
        await session.commit()
    await update.message.reply_text(f"Задача '{task.title}' завершена!")

# /tasks - список активных задач
async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    async with async_session() as session:
        tasks = await Task.get_active_tasks(session, user_id)
        if not tasks:
            await update.message.reply_text("Нет активных задач!")
            return
        msg = '\n'.join([f"- {t.title}" for t in tasks])
        await update.message.reply_text(f"Ваши задачи:\n{msg}")
