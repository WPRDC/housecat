# Generated by Django 5.1.4 on 2025-01-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing_data', '0002_fhlbfundingid_fhlbrentalprojects_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupIndex',
            fields=[
                ('id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('house_cat_id', models.CharField(max_length=100)),
                ('group_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': '0b6a109e-b1f1-4064-8f42-eeb5355dc9df',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParcelIndex',
            fields=[
                ('id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('parcel_id', models.CharField(max_length=100)),
                ('group_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'e82411f8-623d-4336-b714-ecdded80703d',
                'managed': False,
            },
        ),
    ]
