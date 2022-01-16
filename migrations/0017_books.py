# Generated by Django 3.1.1 on 2040-01-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0016_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_title', models.CharField(max_length=100)),
                ('books_url', models.URLField()),
                ('books_file', models.ImageField(blank=True, default='default.png', upload_to='books_icons')),
            ],
        ),
    ]
