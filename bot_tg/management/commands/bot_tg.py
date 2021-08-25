import telebot
import vk_api
from django.core.management import BaseCommand
from vk_api.longpoll import VkLongPoll

from VK_Tg.conf import TOKEN_VK, user_id_vk
from bot_tg.models import TgMsg

bot = telebot.TeleBot('1996894815:AAEGksMKvnrxQ33Is49yZ8ZgouH1vWsryUU')

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


# vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})
@bot.message_handler(content_types=['photo'])
def photo(message):
    if message.photo:
        print("gjhghj")




@bot.message_handler(commands=['replay'])
def start_command(message):
    for msgs in list(TgMsg.objects.all().filter(sent='False')):
        vk_session.method('messages.send', {'user_id': user_id_vk, 'message': msgs, 'random_id': 0})
        TgMsg.objects.all().filter(sent='False').update(sent=True)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler()
def tg_msg(message):
    if message.text:
        msg = message.text.lower()
        TgMsg(msg=msg).save()
        bot.send_message(message.chat.id, 'ok')


bot.polling()


class Command(BaseCommand):
    help = 'Телеграм-бот'
