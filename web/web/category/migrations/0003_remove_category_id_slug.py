# Generated by Django 3.2.9 on 2021-11-09 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_name_test_category_id_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id_slug',
        ),
    ]