# Generated by Django 3.2 on 2022-01-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trailers', '0005_auto_20220123_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailers',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
