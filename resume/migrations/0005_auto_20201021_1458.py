# Generated by Django 3.1.1 on 2020-10-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201014_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='myself',
            name='position',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='myself',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]
