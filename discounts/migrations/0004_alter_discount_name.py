# Generated by Django 4.1 on 2022-08-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0003_discount_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.CharField(default='My_discount_code', max_length=32),
        ),
    ]
