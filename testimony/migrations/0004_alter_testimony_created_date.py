# Generated by Django 3.2.13 on 2022-06-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimony', '0003_auto_20220601_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
