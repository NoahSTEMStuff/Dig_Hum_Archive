# Generated by Django 4.0.5 on 2023-08-02 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0017_genre_genretorecords'),
    ]

    operations = [
        migrations.AddField(
            model_name='associatedimage',
            name='associated_doc1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archive.genretorecords'),
        ),
        migrations.AddField(
            model_name='associatedimage',
            name='associated_doc2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archive.genre'),
        ),
    ]
