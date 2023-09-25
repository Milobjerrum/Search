# Generated by Django 4.2.5 on 2023-09-25 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0007_rename_watchlist_listing_watch"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name="listing",
            old_name="starting_bid",
            new_name="price",
        ),
        migrations.AddField(
            model_name="listing",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="bids",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="comments",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="listing",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="listing",
            name="watch",
            field=models.ManyToManyField(
                related_name="watch", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="auctions.category",
            ),
        ),
    ]