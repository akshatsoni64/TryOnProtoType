# Generated by Django 3.0.1 on 2020-02-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TryOn', '0005_auto_20200218_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]