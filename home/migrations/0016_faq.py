# Generated by Django 2.2.12 on 2023-02-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_feature_featuretitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_question', models.CharField(max_length=200)),
                ('faq_answer', models.TextField()),
            ],
        ),
    ]
