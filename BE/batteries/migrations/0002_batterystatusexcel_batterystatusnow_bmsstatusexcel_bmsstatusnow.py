# Generated by Django 3.2.16 on 2022-11-15 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batteries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BmsStatusNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('now', models.DateTimeField()),
                ('bms', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='batteries.bms')),
            ],
            options={
                'db_table': 'bms_status_now',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BmsStatusExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('now', models.DateTimeField()),
                ('bms', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='batteries.bms')),
            ],
            options={
                'db_table': 'bms_status_excel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BatteryStatusNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.FloatField()),
                ('amount', models.IntegerField()),
                ('now', models.DateTimeField()),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='batteries.battery')),
            ],
            options={
                'db_table': 'battery_status_now',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BatteryStatusExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voltage', models.FloatField()),
                ('amount', models.IntegerField()),
                ('now', models.DateTimeField()),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='batteries.battery')),
            ],
            options={
                'db_table': 'battery_status_excel',
                'managed': True,
            },
        ),
    ]
