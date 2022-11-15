# Generated by Django 4.1.3 on 2022-11-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalNotes', '0006_auther_slug_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auther',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
