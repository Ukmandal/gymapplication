# Generated by Django 5.1.3 on 2024-11-17 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='products_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='products_name',
            new_name='product_name',
        ),
    ]