# Generated by Django 4.2.10 on 2024-03-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltourapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('about', models.TextField()),
            ],
        ),
    ]
