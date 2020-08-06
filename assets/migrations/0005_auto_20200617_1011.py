# Generated by Django 2.2.13 on 2020-06-17 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20200617_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='asset',
            name='teams',
            field=models.ManyToManyField(blank=True, to='users.Team'),
        ),
    ]