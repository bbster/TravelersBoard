# Generated by Django 3.0.8 on 2020-07-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20200715_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
