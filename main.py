# WELCOME 

async def send_welcome(message: types.Message):
    text = (
        "👋 <b>Welcome to the Bestshop Telegram Shop!</b>\n\n"
        "🤖 You can order our entire product catalog automatically here.\n\n"
        "🛍️ To begin, use the <b>/menu</b> command, and view our products!\n"
        "💰 Monero (XMR) & Bitcoin (BTC) accepted.\n\n"
        "❓ Any questions? No problem! Use the <b>/sos</b> command to contact Bestshop Staff.\n\n"
        "🤝 <u>DON'T GET PHISHED.</u> Use official Bestshop sources! Click 🌟 <b>Official Links</b>."
    )
    await message.answer(text, reply_markup=main_reply_kb())
