# Generated by Django 3.2.18 on 2023-04-26 09:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230425_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='project'),
        ),
    ]