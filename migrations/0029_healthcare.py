# Generated by Django 3.1.1 on 2040-01-05 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slaysite', '0028_gdesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthcare_title', models.CharField(max_length=100)),
                ('healthcare_url', models.URLField()),
                ('healthcare_file', models.ImageField(blank=True, default='default.png', upload_to='healthcare_icons')),
            ],
        ),
    ]
