import telebot
import vk_api
from django.core.management import BaseCommand
from vk_api.longpoll import VkLongPoll, VkEventType

from VK_Tg.conf import TOKEN_VK, chat_id_tg, TOKEN_TG
from bot_vk.models import VKmsg

bot = telebot.TeleBot(TOKEN_TG)

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def vk_user_id(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.attachments.get('attach1_type'):
            attachment = event.attachments.get('attach1_type')
            bot.send_message(chat_id_tg, attachment)

        if event.text == 'VK':
            id = event.user_id
            vk_user_id(id, text=f"Привет это ID чата vk: {id}")

        if event.text:
            msg = event.text.lower()
            VKmsg(msg=msg).save()
            for msgs in VKmsg.objects.all().filter(sent='False'):
                bot.send_message(chat_id_tg, msgs)
                VKmsg.objects.all().filter(sent='False').update(sent=True)

bot.polling()


class Command(BaseCommand):
    pass
