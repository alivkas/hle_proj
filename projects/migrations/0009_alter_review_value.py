# Generated by Django 4.2 on 2023-04-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_rename_review_text_review_body_review_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'Положительная оценка'), ('down', 'Отрицательная оценка')], max_length=200),
        ),
    ]