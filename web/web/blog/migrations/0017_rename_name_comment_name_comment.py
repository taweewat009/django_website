# Generated by Django 3.2.9 on 2022-02-21 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='name_comment',
        ),
    ]
