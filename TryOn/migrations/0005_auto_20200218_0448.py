# Generated by Django 3.0.1 on 2020-02-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TryOn', '0004_auto_20200217_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipper',
            name='address_proof',
            field=models.FileField(upload_to='Files'),
        ),
        migrations.AlterField(
            model_name='shipper',
            name='permit_document',
            field=models.FileField(upload_to='Files'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address_proof',
            field=models.FileField(upload_to='Files'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='permit_document',
            field=models.FileField(upload_to='Files'),
        ),
    ]
