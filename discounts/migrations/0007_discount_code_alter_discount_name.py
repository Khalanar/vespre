# Generated by Django 4.1 on 2022-08-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0006_alter_discount_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='code',
            field=models.CharField(default='My_discount_code', max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='name',
            field=models.CharField(default='My_discount_code', max_length=32, unique=True),
        ),
    ]
