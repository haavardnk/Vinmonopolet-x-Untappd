# Generated by Django 3.1.4 on 2020-12-08 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0010_auto_20201208_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='uptappd_id',
            new_name='untappd_id',
        ),
    ]
