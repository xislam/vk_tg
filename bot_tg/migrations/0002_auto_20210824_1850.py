# Generated by Django 3.2.6 on 2021-08-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_tg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TgMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(verbose_name='msg_vk')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
