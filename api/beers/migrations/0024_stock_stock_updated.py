# Generated by Django 3.1.4 on 2020-12-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0023_beer_prioritize_recheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]