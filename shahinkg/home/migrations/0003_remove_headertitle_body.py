# Generated by Django 4.2.5 on 2023-10-08 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_headertitle_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headertitle',
            name='body',
        ),
    ]
