# Generated by Django 3.2.14 on 2022-07-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0008_alter_product_paking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='paking_date',
            field=models.DateField(),
        ),
    ]
