import telebot
import vk_api
from django.core.management import BaseCommand
from vk_api.longpoll import VkLongPoll

from VK_Tg.conf import TOKEN_VK
from bot_tg.models import TgMsg

bot = telebot.TeleBot('1996894815:AAEGksMKvnrxQ33Is49yZ8ZgouH1vWsryUU')

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler()
def tg_msg(message):
    if message.text:
        msg = message.text.lower()
        TgMsg(msg=msg).save()
        bot.send_message(message.chat.id, 'ok')


@bot.message_handler(commands=['Replay'])
def start_command(message):
    for msgs in TgMsg.objects.all():
        tg_msgs = msgs.msg
        bot.send_message(message.chat.id, tg_msgs)


bot.polling()


class Command(BaseCommand):
    help = 'Телеграм-бот'
