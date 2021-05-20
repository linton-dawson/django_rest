# Generated by Django 3.2.3 on 2021-05-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invalid_trigger', models.CharField(default=None, max_length=200)),
                ('values', models.CharField(max_length=200)),
                ('supported_values', models.CharField(default=None, max_length=200)),
                ('support_multiple', models.BooleanField(default=False)),
                ('key', models.CharField(default=None, max_length=200)),
                ('pick_first', models.BooleanField(default=False, max_length=200)),
            ],
        ),
    ]