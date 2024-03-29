# Generated by Django 3.2 on 2022-07-10 17:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_body', models.CharField(max_length=128)),
                ('users', models.ManyToManyField(related_name='todos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
