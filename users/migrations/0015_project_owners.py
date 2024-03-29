# Generated by Django 5.0.1 on 2024-02-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_category_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owners',
            field=models.ManyToManyField(help_text='people involved in this project.', related_name='projects', to='users.userprofile'),
        ),
    ]
