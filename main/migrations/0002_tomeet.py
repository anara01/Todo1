# Generated by Django 3.2.7 on 2021-11-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persone', models.CharField(max_length=30)),
                ('phone_number', models.FloatField()),
                ('date_of_meeting', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
