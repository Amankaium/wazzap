# Generated by Django 3.1.2 on 2020-10-31 13:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_child_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='участники'),
        ),
    ]
