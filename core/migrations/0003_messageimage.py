# Generated by Django 3.1.2 on 2020-10-08 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201008_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='messages/')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_image', to='core.message')),
            ],
        ),
    ]