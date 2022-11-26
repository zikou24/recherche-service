# Generated by Django 3.2.6 on 2022-11-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20221118_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Cenceled', 'Cenceled'), ('Accepted', 'accepted'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderservice',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
