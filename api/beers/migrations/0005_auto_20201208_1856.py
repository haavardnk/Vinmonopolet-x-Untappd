# Generated by Django 3.1.4 on 2020-12-08 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_sitesettings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteSettings',
            new_name='SiteSetting',
        ),
    ]
