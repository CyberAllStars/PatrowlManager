# Generated by Django 2.2.16 on 2020-12-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0004_auto_20201202_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanjob',
            name='position',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='scanjob',
            name='status',
            field=models.CharField(choices=[('started', 'Started'), ('finished', 'Finished'), ('error', 'Error'), ('stopped', 'Stopped')], default='started', max_length=20),
        ),
    ]