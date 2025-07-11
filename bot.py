import logging
import os
from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes, CallbackQueryHandler)
from config import BOT_TOKEN
from handlers.pomodoro import start_pomodoro, pause_pomodoro, skip_break, show_settings
from handlers.tasks import new_project, new_task, focus_task, done_task, list_tasks
from handlers.projects import list_projects
from handlers.gamification import show_forest, show_stats
from handlers.groups import create_group, join_group, group_stats, leaderboard
from db.session import init_db

logging.basicConfig(level=logging.INFO)

async def on_startup(app: Application):
    await init_db()
    logging.info("Bot started and DB initialized.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_pomodoro))
    application.add_handler(CommandHandler("pause", pause_pomodoro))
    application.add_handler(CommandHandler("skipbreak", skip_break))
    application.add_handler(CommandHandler("settings", show_settings))
    application.add_handler(CommandHandler("newproject", new_project))
    application.add_handler(CommandHandler("newtask", new_task))
    application.add_handler(CommandHandler("focus", focus_task))
    application.add_handler(CommandHandler("done", done_task))
    application.add_handler(CommandHandler("tasks", list_tasks))
    application.add_handler(CommandHandler("projects", list_projects))
    application.add_handler(CommandHandler("forest", show_forest))
    application.add_handler(CommandHandler("stats", show_stats))
    application.add_handler(CommandHandler("creategroup", create_group))
    application.add_handler(CommandHandler("joingroup", join_group))
    application.add_handler(CommandHandler("groupstats", group_stats))
    application.add_handler(CommandHandler("leaderboard", leaderboard))

    application.run_polling(stop_signals=None)

if __name__ == "__main__":
    main()
