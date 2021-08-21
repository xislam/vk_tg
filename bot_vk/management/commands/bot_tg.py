from django.core.management import BaseCommand
from django.db.migrations import executor


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(vk)
