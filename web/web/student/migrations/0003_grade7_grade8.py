# Generated by Django 3.2.9 on 2021-11-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_grade_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('subject1', models.CharField(max_length=100)),
                ('subject2', models.CharField(max_length=100)),
                ('comsci_score', models.IntegerField()),
                ('comsci_Grade', models.CharField(max_length=50)),
                ('tech_score', models.IntegerField()),
                ('tech_Grade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grade8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('subject1', models.CharField(max_length=100)),
                ('subject2', models.CharField(max_length=100)),
                ('comsci_score', models.IntegerField()),
                ('comsci_Grade', models.CharField(max_length=50)),
                ('tech_score', models.IntegerField()),
                ('tech_Grade', models.CharField(max_length=50)),
            ],
        ),
    ]