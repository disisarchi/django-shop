# Generated by Django 4.0.8 on 2024-08-14 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_review_description_review_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
