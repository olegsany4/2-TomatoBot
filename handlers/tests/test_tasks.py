import pytest
from telegram import Update
from telegram.ext import ContextTypes
from handlers.tasks import new_task

@pytest.mark.asyncio
async def test_new_task():
    update = Update(update_id=1, message=None)
    context = ContextTypes.DEFAULT_TYPE()
    await new_task(update, context)
