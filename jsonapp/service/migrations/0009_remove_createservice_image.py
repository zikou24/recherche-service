# Generated by Django 3.2.6 on 2022-11-10 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_createservice_your_sertificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createservice',
            name='image',
        ),
    ]