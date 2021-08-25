from django.contrib import admin

# Register your models here.
from bot_tg.models import TgMsg

admin.site.register(TgMsg)