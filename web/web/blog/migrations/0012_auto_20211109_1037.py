# Generated by Django 3.2.9 on 2021-11-09 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blogs_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='name_cate',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='slug',
        ),
    ]
