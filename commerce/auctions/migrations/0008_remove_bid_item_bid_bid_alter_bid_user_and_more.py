# Generated by Django 4.1.4 on 2023-01-09 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_comment_comment_message_remove_comment_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='item',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_price', to='auctions.bid'),
        ),
    ]
