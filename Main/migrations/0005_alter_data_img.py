# Generated by Django 4.2.2 on 2024-03-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_data_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='img',
            field=models.FileField(default='static/imgs/1.jpeg', null=True, upload_to='static/imgs/'),
        ),
    ]
