# Generated by Django 4.0.6 on 2022-08-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='public',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
