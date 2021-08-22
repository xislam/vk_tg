import vk
import vk_api
from django.core.management import BaseCommand
from vk_api.longpoll import VkLongPoll, VkEventType

from VK_Tg.conf import TOKEN_VK
from bot_vk.models import VKmsg

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.text:
            msg = event.text.lower()
            id = event.user_id
            if msg:
                VKmsg(msg=msg).save()



class Command(BaseCommand):
    pass
