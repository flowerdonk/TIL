# Generated by Django 3.2.12 on 2023-04-11 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
