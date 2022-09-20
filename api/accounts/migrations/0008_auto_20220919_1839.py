# Generated by Django 3.2 on 2022-09-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_userprofile_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='expected_account_tenure',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]