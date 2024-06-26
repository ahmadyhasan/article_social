# Generated by Django 4.2.7 on 2024-02-09 20:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Name')),
            ],
            options={
                'ordering': ('-create_time',),
                'abstract': False,
            },
        ),
    ]
