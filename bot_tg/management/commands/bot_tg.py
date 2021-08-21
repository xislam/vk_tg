from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from django.core.management import BaseCommand

from VK_Tg.conf import TOKEN_TG

bot = Bot(token=TOKEN_TG)
tg = Dispatcher(bot, storage=MemoryStorage())


@tg.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привет! тут будет текст")


@tg.message_handler()
async def process_start_command(message: types.Message):
    text = message.text
    print(text)
    await message.reply(text)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(tg)
