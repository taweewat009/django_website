# Generated by Django 3.2.9 on 2021-11-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogs_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='category_name',
            field=models.CharField(max_length=200),
        ),
    ]
