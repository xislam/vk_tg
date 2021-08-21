from django.core.management import BaseCommand
from aiogram.utils import executor


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(vk)
