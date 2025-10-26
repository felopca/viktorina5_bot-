import random

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InputMediaPhoto, ForceReply
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
import asyncio




app = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="my_cool_bot",
)
buttons = [
        [InlineKeyboardButton("Кнопка 1", callback_data="button1")],
        [InlineKeyboardButton("Кнопка 2", callback_data="button2")]
    ]
# Обработчик команды /start
@app.on_message(filters.command("start"))
def start_command(client, message):
    random.shuffle(buttons)
    keyboard = InlineKeyboardMarkup(buttons)
    message.reply_text("Ответ с клавиатурой", reply_markup=keyboard)

# Обработчик нажатий на кнопки
@app.on_callback_query()
def handle_callback_query(client, query):
    if query.data == "button1":
        # Действия при нажатии на кнопку 1
        query.message.edit_text("+++")
    else:
        # Действия при нажатии на кнопку 2
        query.message.edit_text("---")







app.run()

