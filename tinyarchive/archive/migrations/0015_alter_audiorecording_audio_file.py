# Generated by Django 4.0.5 on 2023-08-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0014_rename_creator_archivedocument_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiorecording',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='sounds/'),
        ),
    ]
