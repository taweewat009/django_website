# Generated by Django 3.2.9 on 2021-11-04 06:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
