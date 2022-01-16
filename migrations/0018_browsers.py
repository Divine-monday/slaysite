# Generated by Django 3.1.1 on 2040-01-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0017_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Browsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browsers_title', models.CharField(max_length=100)),
                ('browsers_url', models.URLField()),
                ('browsers_file', models.ImageField(blank=True, default='default.png', upload_to='browsers_icons')),
            ],
        ),
    ]