# Generated by Django 3.1.1 on 2040-01-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0024_fashion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gaming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gaming_title', models.CharField(max_length=100)),
                ('gaming_url', models.URLField()),
                ('gaming_file', models.ImageField(blank=True, default='default.png', upload_to='gaming_icons')),
            ],
        ),
    ]