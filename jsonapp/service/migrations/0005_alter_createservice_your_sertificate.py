# Generated by Django 3.2.6 on 2022-11-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_createservice_wilaya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createservice',
            name='your_sertificate',
            field=models.FileField(upload_to='photos/competence'),
        ),
    ]
