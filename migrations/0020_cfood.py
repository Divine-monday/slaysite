# Generated by Django 3.1.1 on 2040-01-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0019_cartoons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cfood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfood_title', models.CharField(max_length=100)),
                ('cfood_url', models.URLField()),
                ('cfood_file', models.ImageField(blank=True, default='default.png', upload_to='cfood_icons')),
            ],
        ),
    ]