# Generated by Django 3.0.4 on 2020-07-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200713_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nancy',
            name='imagefile',
            field=models.ImageField(null=True, upload_to='nancy/images'),
        ),
    ]
