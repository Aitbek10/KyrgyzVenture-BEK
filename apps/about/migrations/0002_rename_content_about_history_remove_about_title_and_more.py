# Generated by Django 5.1.2 on 2024-10-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='content',
            new_name='history',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title',
        ),
        migrations.AddField(
            model_name='about',
            name='mission',
            field=models.TextField(default='Стандартная миссия'),
        ),
        migrations.AddField(
            model_name='about',
            name='vision',
            field=models.TextField(default='Стандартное видение'),
        ),
    ]
