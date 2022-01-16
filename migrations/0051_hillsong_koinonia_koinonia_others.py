# Generated by Django 3.1.1 on 2022-01-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0050_abouticons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hillsong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hillsong_title', models.CharField(max_length=100)),
                ('hillsong_url', models.URLField()),
                ('hillsong_file', models.ImageField(blank=True, default='default.png', upload_to='hillsong_icons')),
            ],
        ),
        migrations.CreateModel(
            name='Koinonia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koinonia_title', models.CharField(max_length=100)),
                ('koinonia_url', models.URLField()),
                ('koinonia_file', models.ImageField(blank=True, default='default.png', upload_to='koinonia_icons')),
            ],
        ),
        migrations.CreateModel(
            name='Koinonia_Others',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koothers_title', models.CharField(max_length=100)),
                ('koothers_url', models.URLField()),
                ('koothers_file', models.ImageField(blank=True, default='default.png', upload_to='koothers_icons')),
            ],
        ),
    ]