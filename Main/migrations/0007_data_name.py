# Generated by Django 4.2.2 on 2024-03-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_video_remove_data_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]