# Generated by Django 3.2.4 on 2021-06-29 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapSpeech_app', '0010_alter_requests_request_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patientDiagnosis',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='patient',
            name='patientMedicalHistory',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='patient',
            name='patientMedication',
            field=models.TextField(default='', max_length=5000),
        ),
    ]
