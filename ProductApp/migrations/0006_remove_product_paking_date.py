# Generated by Django 3.2.14 on 2022-07-26 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0005_alter_product_paking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='paking_date',
        ),
    ]
