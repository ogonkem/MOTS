# Generated by Django 3.2.13 on 2022-05-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimony', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/testimony'),
        ),
    ]