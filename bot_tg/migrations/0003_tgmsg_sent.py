# Generated by Django 3.2.6 on 2021-08-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_tg', '0002_auto_20210824_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgmsg',
            name='sent',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]