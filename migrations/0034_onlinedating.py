# Generated by Django 3.1.1 on 2022-01-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0033_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineDating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online_dating_title', models.CharField(max_length=100)),
                ('online_dating_url', models.URLField()),
                ('online_dating_file', models.ImageField(blank=True, default='default.png', upload_to='online_dating_icons')),
            ],
        ),
    ]