# Generated by Django 4.2 on 2023-04-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_review_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, default='profile_images/default.jpg', null=True, upload_to='profile_images'),
        ),
    ]