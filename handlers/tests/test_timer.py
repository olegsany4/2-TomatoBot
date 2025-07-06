import pytest
from telegram import Update
from telegram.ext import ContextTypes
from services.timer import PomodoroTimer

@pytest.mark.asyncio
async def test_start_pomodoro():
    # Мок-объекты update/context
    update = Update(update_id=1, message=None)
    context = ContextTypes.DEFAULT_TYPE()
    # Проверка, что не выбрасывает исключений
    await PomodoroTimer.start(update, context)
