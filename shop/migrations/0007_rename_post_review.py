# Generated by Django 4.0.8 on 2024-08-12 16:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_basketitem_created_at_course_created_at_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Review',
        ),
    ]