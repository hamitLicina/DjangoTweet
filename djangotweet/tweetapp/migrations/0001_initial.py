# Generated by Django 5.1.3 on 2024-11-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
