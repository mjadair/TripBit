# Generated by Django 3.0.2 on 2020-01-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0003_group_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.CharField(default='https://cdn.pixabay.com/photo/2014/04/02/10/47/globe-304586_1280.png', max_length=500),
        ),
    ]