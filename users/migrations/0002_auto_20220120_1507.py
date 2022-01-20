# Generated by Django 2.2.5 on 2022-01-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
