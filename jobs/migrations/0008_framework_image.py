# Generated by Django 3.1.1 on 2020-10-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20201015_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='framework',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
