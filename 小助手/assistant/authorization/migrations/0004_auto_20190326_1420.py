# Generated by Django 2.1 on 2019-03-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_eshi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eshi',
            name='focus_stock',
            field=models.TextField(default='[]'),
        ),
    ]
