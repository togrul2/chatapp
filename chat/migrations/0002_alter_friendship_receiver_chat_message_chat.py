# Generated by Django 4.0.5 on 2022-06-26 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.friendship')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.chat'),
            preserve_default=False,
        ),
    ]
