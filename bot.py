from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
AUTHORIZED_USER_ID = int(os.getenv("AUTHORIZED_USER_ID"))

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == AUTHORIZED_USER_ID:
        await update.message.reply_text("Ты отправил текст.")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == AUTHORIZED_USER_ID:
        await update.message.reply_text("Ты отправил фото.")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == AUTHORIZED_USER_ID:
        await update.message.reply_text("Ты отправил видео.")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == AUTHORIZED_USER_ID:
        await update.message.reply_text("Ты отправил голосовое сообщение.")

async def handle_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == AUTHORIZED_USER_ID:
        await update.message.reply_text("Ты отправил аудио файл.")

async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == AUTHORIZED_USER_ID:
        await update.message.reply_text("Ты отправил стикер.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.AUDIO, handle_audio))
    app.add_handler(MessageHandler(filters.Sticker.ALL, handle_sticker))
