from telegram import Update
from telegram.ext import ContextTypes

GUIDE_STEPS = [
    "1️⃣ Что такое Техника помидора?\n25 минут работы, 5 минут отдыха. Повтор 4 раза — длинный перерыв.",
    "2️⃣ Что такое проект и задача?\nПроект — большая цель. Задача — конкретное действие.",
    "3️⃣ Как создать проект?\nКоманда: /newproject Название", 
    "4️⃣ Как создать задачу и сфокусироваться?\nКоманды: /newtask, /focus",
    "5️⃣ Как удалить, редактировать, завершить проект?\nКоманды: /edit, /delete, /done",
    "6️⃣ Что такое 'томат'?\nОдин интервал фокусированной работы."
]

async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    step = int(context.user_data.get('guide_step', 0))
    msg = f"🍅\n{GUIDE_STEPS[step]}"
    keyboard = []
    if step < len(GUIDE_STEPS) - 1:
        keyboard = [[{"text": "Далее", "callback_data": "guide_next"}]]
    await update.message.reply_text(msg)
    context.user_data['guide_step'] = step + 1 if step < len(GUIDE_STEPS) - 1 else 0
