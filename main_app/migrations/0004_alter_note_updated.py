# Generated by Django 5.0.6 on 2024-06-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_note_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="updated",
            field=models.DateField(auto_now=True),
        ),
    ]
