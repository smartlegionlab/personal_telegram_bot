# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

from utils.configs import ConfigLoader

load_dotenv()

logging.basicConfig(level=logging.INFO)


class TelegramBot:

    def __init__(self, token: str, admin_id):
        self.app_config = ConfigLoader('.config.json')
        self.app_config.load_config()
        self.admin_id = admin_id
        self.bot = Bot(
            token=token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML
            )
        )
        self.dp = Dispatcher()
        self.dp.message(Command("start"))(self.cmd_start)
        self.dp.message()(self.echo_handler)
        self.dp.callback_query()(self.callback_handler)

    async def cmd_start(self, message: types.Message):
        name = self.app_config.get_company_name()
        description = self.app_config.get_company_description()
        url = self.app_config.get_company_url()
        msg = f"<b>{name}</b>\n\n{description}\n\nSend us a message:"
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Open Site", url=url)
        )
        await message.answer(msg, reply_markup=builder.as_markup())

    async def echo_handler(self, message: Message) -> None:
        user_info = message.from_user
        user_name = user_info.full_name
        user_id = user_info.id
        username = user_info.username
        if username:
            user_link = f'https://t.me/{username}'
        else:
            user_link = f'ID: {user_id}'
        admin_message = f'Message from {user_name} ({user_link}):\n\n{message.text}'
        await self.bot.send_message(chat_id=self.admin_id, text=admin_message)
        await message.answer(f'Thank you {message.from_user.full_name}! '
                             f'Your message has been sent. {self.app_config.get_company_name()}.')
        await self.cmd_start(message)

    async def callback_handler(self, callback_query: types.CallbackQuery) -> None:
        if callback_query.data == "back_to_start":
            await self.cmd_start(callback_query.message)

    async def run(self):
        await self.dp.start_polling(self.bot)


def main():
    api_token = os.getenv("PERSONAL_API_TOKEN")
    admin_chat_id = os.getenv("ADMIN_CHAT_ID")
    telegram_bot = TelegramBot(api_token, admin_chat_id)
    asyncio.run(telegram_bot.run())


if __name__ == "__main__":
    main()
