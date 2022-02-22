# Generated by Django 3.2.9 on 2022-02-21 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_slug'),
        ('blog', '0018_alter_blogs_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
