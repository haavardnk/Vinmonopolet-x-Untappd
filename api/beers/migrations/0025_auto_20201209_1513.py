# Generated by Django 3.1.4 on 2020-12-09 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0024_stock_stock_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='updated_at',
            new_name='store_updated',
        ),
    ]
