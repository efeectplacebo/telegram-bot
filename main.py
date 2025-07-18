import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def join_request_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    keyboard = [
        [InlineKeyboardButton("🎁 Забрати бонус", url="https://track.stream-gh.shop/sl?id=687a0b103913fc6f4740965e&pid=3777&sub1=link1")],
        [InlineKeyboardButton("📋 Інструкція", url="https://t.me/gghhyg")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        f"Alibaba, Привіт 👋\n\n"
        f"Ти за адресою)\n"
        f"Трансляція реваншу буде тут 😉\n\n"
        f"Всі ми знаємо хто переможе 😉\n"
        f"То чому б на цьому не заробити? 😁\n\n"
        f"Хочеш зробити ставку на нашого чемпіона 👇\n"
        f"Від мене отримуєш до 50 000 грн на перший депозит 🔥\n\n"
        f"Слава Україні 🇺🇦"
    )

    await context.bot.send_message(chat_id=user.id, text=text, reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(join_request_handler))
    app.run_polling()
