# Generated by Django 3.1.1 on 2022-01-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0043_tv_shows'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos_title', models.CharField(max_length=100)),
                ('videos_url', models.URLField()),
                ('videos_file', models.ImageField(blank=True, default='default.png', upload_to='videos_icons')),
            ],
        ),
    ]
