from django.db import models


class VKmsg(models.Model):
    msg = models.TextField(verbose_name='msg_vk')

    def __str__(self):
        return self.msg
