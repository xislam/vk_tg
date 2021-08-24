from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from asgiref.sync import sync_to_async
from django.core.management import BaseCommand

from VK_Tg.conf import TOKEN_TG
from bot_vk.models import VKmsg

bot = Bot(token=TOKEN_TG)
tg = Dispatcher(bot, storage=MemoryStorage())


@tg.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    m = message.chat.id
    print(m)
    await message.reply(f"Привет! тут будет текст")


@tg.message_handler()
async def process_start_command(text):

    await bot.send_message('-1001516737166', text)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(tg)
