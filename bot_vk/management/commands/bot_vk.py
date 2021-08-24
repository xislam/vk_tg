import telebot
import vk_api
from django.core.management import BaseCommand
from vk_api.longpoll import VkLongPoll, VkEventType

from VK_Tg.conf import TOKEN_VK
from bot_vk.models import VKmsg

bot = telebot.TeleBot('1996894815:AAEGksMKvnrxQ33Is49yZ8ZgouH1vWsryUU')

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def sender_vk(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        print(event.attachments)

        if event.text:
            msg = event.text.lower()
            id = event.user_id
            if msg:
                VKmsg(msg=msg).save()
                bot.send_message(-1001516737166, msg)

            if event.attachments:

                bot.send_message(-1001516737166, event.attachments)


bot.polling()


class Command(BaseCommand):
    pass
