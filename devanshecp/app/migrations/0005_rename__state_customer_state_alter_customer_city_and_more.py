# Generated by Django 4.2.6 on 2023-12-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='_state',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='locality',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
