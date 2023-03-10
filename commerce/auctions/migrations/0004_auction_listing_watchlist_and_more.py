# Generated by Django 4.1.4 on 2023-01-08 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_ower_auction_listing_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='list_watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='imageURL',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='auction_listing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
