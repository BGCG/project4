# Generated by Django 3.2.18 on 2023-05-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230521_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='question_type',
            field=models.CharField(choices=[(None, 'How can we help?'), ('Accounts', "There's something wrong with my account"), ('Feedback', 'I would like to provide some feedback'), ('Complaint', 'I would like to make a complaint'), ('Technical issue', 'I would like to report a technical issue'), ('Other', 'Other')], max_length=80),
        ),
    ]
