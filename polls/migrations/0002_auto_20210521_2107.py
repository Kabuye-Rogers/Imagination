# Generated by Django 3.1.5 on 2021-05-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qout',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
