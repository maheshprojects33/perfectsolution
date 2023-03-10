# Generated by Django 2.2.12 on 2023-02-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(max_length=50)),
                ('hero_detail', models.TextField()),
                ('hero_img', models.ImageField(blank=True, upload_to='hero')),
                ('hero_logo', models.ImageField(blank=True, upload_to='hero')),
            ],
        ),
    ]
