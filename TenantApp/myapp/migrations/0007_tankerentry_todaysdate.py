# Generated by Django 4.2.1 on 2023-10-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_month_submeter_amount_remove_submeter_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='tankerentry',
            name='todaysdate',
            field=models.CharField(default='0', max_length=20),
        ),
    ]