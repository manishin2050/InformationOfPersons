# Generated by Django 4.2.2 on 2024-03-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_alter_data_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, null=True)),
                ('code', models.IntegerField()),
                ('title', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='name',
        ),
    ]
