# Generated by Django 2.2.7 on 2020-01-29 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='cat',
        ),
        migrations.DeleteModel(
            name='item',
        ),
    ]
