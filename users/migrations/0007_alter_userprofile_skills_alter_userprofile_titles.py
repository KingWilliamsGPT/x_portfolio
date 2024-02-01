# Generated by Django 5.0.1 on 2024-01-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(to='users.skill'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='titles',
            field=models.ManyToManyField(to='users.title'),
        ),
    ]
