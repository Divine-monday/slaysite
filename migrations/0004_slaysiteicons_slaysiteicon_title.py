# Generated by Django 3.1.1 on 2040-01-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0003_slaysiteicons'),
    ]

    operations = [
        migrations.AddField(
            model_name='slaysiteicons',
            name='slaysiteicon_title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]