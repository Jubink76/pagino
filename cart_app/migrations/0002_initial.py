# Generated by Django 5.1.2 on 2024-10-16 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart_app', '0001_initial'),
        ('log_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carttable',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='log_reg_app.usertable'),
        ),
    ]
