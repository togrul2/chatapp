# Generated by Django 4.0.5 on 2022-07-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_options_alter_blog_author_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
