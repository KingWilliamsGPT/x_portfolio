# Generated by Django 5.0.1 on 2024-02-02 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_userprofile_designs_made_userprofile_happy_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='name your projects', max_length=255)),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(help_text='Image to display project', upload_to='project_images')),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(help_text='eg. Web design, Graphics Design, Blockchain, Games', on_delete=django.db.models.deletion.CASCADE, to='users.category')),
            ],
        ),
    ]
