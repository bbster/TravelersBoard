# Generated by Django 3.0.8 on 2020-07-21 05:16

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20200717_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
