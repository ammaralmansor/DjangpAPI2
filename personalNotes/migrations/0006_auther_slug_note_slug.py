# Generated by Django 4.1.3 on 2022-11-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalNotes', '0005_alter_auther_options_alter_note_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='auther',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
