# Generated by Django 4.1 on 2022-08-11 11:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0002_delete_discounttype_discount_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]