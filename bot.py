import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8938010090:AAEKfeoEnug2EoWJM8NfftKArHaWyTq2RB8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً يا إسماعيل! البوت شغال وسيرفرك أونلاين 24 ساعة.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"وصلتني رسالتك: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
