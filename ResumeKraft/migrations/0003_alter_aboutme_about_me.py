# Generated by Django 4.1.7 on 2023-12-06 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumeKraft', '0002_alter_aboutme_id_alter_achievements_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about_me',
            field=models.CharField(default='', max_length=200),
        ),
    ]
