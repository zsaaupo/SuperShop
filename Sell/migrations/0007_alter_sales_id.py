# Generated by Django 4.2.1 on 2023-05-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sell', '0006_alter_sales_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
