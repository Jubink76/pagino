# Generated by Django 5.1.2 on 2024-10-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside_app', '0002_rename_image_categorytable_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytable',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]