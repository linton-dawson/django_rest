# Generated by Django 3.2.3 on 2021-05-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20210518_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invalid_trigger', models.CharField(default=None, max_length=200)),
                ('key', models.CharField(default=None, max_length=200)),
                ('support_multiple', models.BooleanField(default=False)),
                ('pick_first', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=1000)),
                ('constraint', models.CharField(default=None, max_length=500)),
                ('var_name', models.CharField(default=None, max_length=10)),
                ('values', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameModel(
            old_name='Slot',
            new_name='Slot1',
        ),
    ]