# Generated by Django 5.0.1 on 2024-02-21 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_message_room_alter_message_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='sender',
        ),
    ]
