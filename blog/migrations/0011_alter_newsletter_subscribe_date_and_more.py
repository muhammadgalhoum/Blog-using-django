# Generated by Django 4.1.6 on 2023-03-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='subscribe_date',
            field=models.DateTimeField(default='2023-03-20 13:21:14'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default='2023-03-20 13:21:14'),
        ),
    ]
