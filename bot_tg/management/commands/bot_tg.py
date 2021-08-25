import telebot
import vk_api
from django.core.management import BaseCommand
from vk_api.longpoll import VkLongPoll

from VK_Tg.conf import TOKEN_VK, user_id_vk, TOKEN_TG
from bot_tg.models import TgMsg

bot = telebot.TeleBot(TOKEN_TG)

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


@bot.message_handler(commands=['replay'])
def replay_command(message):
    for msgs in list(TgMsg.objects.all().filter(sent='False')):
        vk_session.method('messages.send', {'user_id': user_id_vk,
                                            'message': msgs, 'random_id': 0})
        TgMsg.objects.all().filter(sent='False').update(sent=True)


@bot.message_handler(commands=['start'])
def start_command(message):
    tg_id = message.chat.id
    bot.send_message(message.chat.id, f"Привет это ID чата: {tg_id}")


@bot.message_handler()
def tg_msg(message):
    if message.text:
        msg = message.text.lower()
        TgMsg(msg=msg).save()
        bot.send_message(message.chat.id, 'ok')


bot.polling()


class Command(BaseCommand):
    help = 'Телеграм-бот'
