# Generated by Django 4.2.1 on 2023-10-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mainmeter_submeter_tankerentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantname',
            name='todaysdate',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='tenantname',
            name='Address',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='tenantname',
            name='Adhar',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='tenantname',
            name='FlatNumber',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='tenantname',
            name='name',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='tenantname',
            name='phone',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='tenantname',
            name='rent',
            field=models.CharField(default='0', max_length=20),
        ),
    ]