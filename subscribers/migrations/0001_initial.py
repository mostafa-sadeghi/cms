# Generated by Django 3.2.5 on 2022-04-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='email address', max_length=100)),
                ('full_name', models.CharField(help_text='first and last name', max_length=100)),
            ],
        ),
    ]
