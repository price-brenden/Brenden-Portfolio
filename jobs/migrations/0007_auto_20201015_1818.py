# Generated by Django 3.1.1 on 2020-10-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20201015_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastenoframework',
            name='job',
        ),
        migrations.AddField(
            model_name='jobnoframework',
            name='paste',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PasteForFramework',
        ),
        migrations.DeleteModel(
            name='PasteNoFramework',
        ),
    ]
