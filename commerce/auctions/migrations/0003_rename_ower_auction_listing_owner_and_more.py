# Generated by Django 4.1.4 on 2023-01-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_auction_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction_listing',
            old_name='ower',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='description',
            field=models.CharField(max_length=280),
        ),
    ]