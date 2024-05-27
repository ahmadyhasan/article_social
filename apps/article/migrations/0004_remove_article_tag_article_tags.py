# Generated by Django 4.2.7 on 2024-02-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('article', '0003_article_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(db_index=True, related_name='articles', to='tag.tag', verbose_name='Tags'),
        ),
    ]
