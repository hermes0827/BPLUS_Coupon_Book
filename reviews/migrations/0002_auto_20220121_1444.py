# Generated by Django 2.2.5 on 2022-01-21 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='청결도'),
        ),
        migrations.AlterField(
            model_name='review',
            name='deliciousness',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='맛'),
        ),
        migrations.AlterField(
            model_name='review',
            name='kindness',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='친절도'),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='접근성'),
        ),
        migrations.AlterField(
            model_name='review',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store', verbose_name='가게'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='리뷰어'),
        ),
    ]
