# Generated by Django 5.1 on 2024-10-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
