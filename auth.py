# auth.py
from aiogram import types
from aiogram.fsm.context import FSMContext
from states import AuthStates
from keyboards import main_reply_kb

async def check_password(message: types.Message, state: FSMContext):
    if message.text == "PWBots":         // Here the password is "PWBots"
        await message.answer("Password correct ✅")
        await state.set_state(AuthStates.WAITING_CAPTCHA)
    else:
        await message.answer("❌ Wrong password. Try again.")  // If the user types something else, the bot will reject it.
