import asyncio

from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, filters, Updater, ApplicationBuilder, ContextTypes

from gemini_ai import get_gemini_response

# Your Telegram Bot API token
TELEGRAM_API_TOKEN = '7958040791:AAF79eUPFA9013PTigfqH_QjotNgqJwOZOA'

bot = Bot(token=TELEGRAM_API_TOKEN)

async def send_telegram_message(chat_id, text):
    app=ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
    await app.bot.send_message(chat_id=chat_id, text=text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages."""
    user_message = update.message.text
    chat_id = update.message.chat.id

    # Here, you can integrate your AI response logic using the Gemini API
    # For simplicity, we will echo the message back
    # response_message = f"You said: {user_message}"
    response_message=get_gemini_response(user_message)
    await send_telegram_message(chat_id, response_message)

def start_bot():
    """Start the Telegram bot."""
    app = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    app.add_handler(CommandHandler("start", lambda update, context: send_telegram_message(update.effective_chat.id, "Welcome!")))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

def run_bot():
    """Run the Telegram bot in a separate asyncio event loop."""
    asyncio.run(start_bot())