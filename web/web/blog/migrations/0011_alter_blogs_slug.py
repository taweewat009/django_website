# Generated by Django 3.2.9 on 2021-11-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20211109_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
