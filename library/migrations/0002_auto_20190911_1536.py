# Generated by Django 2.2.4 on 2019-09-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ieee_id',
            field=models.CharField(default=0, max_length=12, unique=True),
        ),
    ]
