# Generated by Django 2.2.7 on 2020-03-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0007_auto_20200318_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=4000),
        ),
    ]