# Generated by Django 3.2 on 2021-06-01 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PFES6', '0003_auto_20210601_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='course',
            new_name='courseId',
        ),
    ]
