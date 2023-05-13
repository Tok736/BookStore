# Generated by Django 4.0.5 on 2022-06-14 21:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_book_creator"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={
                "ordering": ["title"],
                "permissions": [("special_status", "Can read all books")],
            },
        ),
        migrations.AddField(
            model_name="review",
            name="date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]