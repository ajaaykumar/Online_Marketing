# Generated by Django 2.1.4 on 2018-12-09 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product_App', '0002_auto_20181209_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='phone_no',
            new_name='phoneno',
        ),
    ]
