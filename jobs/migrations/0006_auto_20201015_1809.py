# Generated by Django 3.1.1 on 2020-10-15 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20201015_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pasteforframework',
            old_name='project',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='pastenoframework',
            old_name='project',
            new_name='job',
        ),
    ]
