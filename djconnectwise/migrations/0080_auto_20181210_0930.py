# Generated by Django 2.0 on 2018-12-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0079_auto_20181203_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
