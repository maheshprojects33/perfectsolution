# Generated by Django 2.2.12 on 2023-02-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_servicetitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurClientLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_logo', models.ImageField(upload_to='client_logo')),
            ],
        ),
        migrations.CreateModel(
            name='OurClientTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_title', models.CharField(max_length=50)),
            ],
        ),
    ]
