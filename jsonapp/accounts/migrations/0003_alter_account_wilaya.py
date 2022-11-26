# Generated by Django 3.2.6 on 2022-11-04 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('accounts', '0002_account_wilaya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='wilaya',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Account', to='service.wilaya'),
        ),
    ]