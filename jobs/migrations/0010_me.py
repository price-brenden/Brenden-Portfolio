# Generated by Django 3.1.1 on 2020-10-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20201021_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.TextField()),
            ],
        ),
    ]
