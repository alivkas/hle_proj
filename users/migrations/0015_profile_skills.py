# Generated by Django 4.2 on 2023-05-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, to='users.skill'),
        ),
    ]
