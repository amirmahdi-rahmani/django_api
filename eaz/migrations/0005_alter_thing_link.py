# Generated by Django 5.0 on 2023-12-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eaz', '0004_thing_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='link',
            field=models.URLField(),
        ),
    ]
