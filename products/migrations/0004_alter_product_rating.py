# Generated by Django 4.1 on 2022-08-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
