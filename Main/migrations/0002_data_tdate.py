# Generated by Django 4.2.2 on 2024-03-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='tdate',
            field=models.DateField(null=True),
        ),
    ]
