# Generated by Django 3.2.15 on 2022-08-10 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Freakin Awesome Blog', max_length=255),
        ),
    ]
