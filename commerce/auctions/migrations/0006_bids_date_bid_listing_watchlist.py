# Generated by Django 4.2.5 on 2023-09-22 09:10

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_alter_listing_seller"),
    ]

    operations = [
        migrations.AddField(
            model_name="bids",
            name="date_bid",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="listing",
            name="watchlist",
            field=models.ManyToManyField(
                related_name="watchlist", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]