# Generated by Django 4.0.6 on 2022-08-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_topic_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.BooleanField(choices=[(False, 'Private'), (True, 'Public')]),
        ),
    ]