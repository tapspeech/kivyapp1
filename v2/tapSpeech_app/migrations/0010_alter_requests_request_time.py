# Generated by Django 3.2.4 on 2021-06-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapSpeech_app', '0009_remove_caretaker_caretakeremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='request_time',
            field=models.CharField(default='', max_length=30),
        ),
    ]