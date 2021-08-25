from django.db import models


class VKmsg(models.Model):
    msg = models.TextField(verbose_name='msg_vk')
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.msg
