# Generated by Django 2.2.12 on 2023-02-13 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_ourclientlogo_ourclienttitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_email',
        ),
    ]
