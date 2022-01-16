# Generated by Django 3.1.1 on 2022-01-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0044_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_title', models.CharField(max_length=100)),
                ('weather_url', models.URLField()),
                ('weather_file', models.ImageField(blank=True, default='default.png', upload_to='weather_icons')),
            ],
        ),
    ]