# Generated by Django 3.2.4 on 2021-06-23 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapSpeech_app', '0004_auto_20210621_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='request_patient',
            field=models.CharField(default='', max_length=30),
        ),
    ]
