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
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        id = event.user_id
        print(id)
        if event.attachments.get('attach1_type'):
            attachment = event.attachments.get('attach1_type')
            bot.send_message(-1001516737166, attachment)

        if event.user_id != '670616148':
            if event.text:
                msg = event.text.lower()
                VKmsg(msg=msg).save()
                for msgs in list(VKmsg.objects.all().filter(sent='False')):
                    bot.send_message(-1001516737166, msgs)

bot.polling()


class Command(BaseCommand):
    pass
