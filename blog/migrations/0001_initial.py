# Generated by Django 4.1.2 on 2022-10-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('tittle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
