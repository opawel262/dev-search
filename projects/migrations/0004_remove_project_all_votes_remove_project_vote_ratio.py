# Generated by Django 4.2.5 on 2023-09-08 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_tag_rename_created_project_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='all_votes',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_ratio',
        ),
    ]
