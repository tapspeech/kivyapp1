# Generated by Django 3.2.4 on 2021-06-30 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapSpeech_app', '0014_auto_20210630_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientEmergencyContact',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientEmergencyContact2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientEmergencyContact3',
            field=models.CharField(default='', max_length=30),
        ),
    ]
