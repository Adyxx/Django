# Generated by Django 3.1.7 on 2021-03-02 15:40

from django.db import migrations, models
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=movies.models.poster_path, verbose_name='Poster'),
        ),
    ]
