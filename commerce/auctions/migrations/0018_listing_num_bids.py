# Generated by Django 4.1.4 on 2023-01-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_listing_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='num_bids',
            field=models.IntegerField(default=1),
        ),
    ]
