# Generated by Django 3.2.18 on 2023-05-29 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_recipe_preparation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)]),
        ),
    ]