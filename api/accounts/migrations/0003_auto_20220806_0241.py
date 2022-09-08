# Generated by Django 3.2 on 2022-08-06 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220806_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='affiliation',
        ),
        migrations.RemoveField(
            model_name='user',
            name='agreed_to_terms',
        ),
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='conflicts',
        ),
        migrations.RemoveField(
            model_name='user',
            name='expected_account_tenure',
        ),
        migrations.RemoveField(
            model_name='user',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='intended_use',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('nonprofit', 'Housing and community development-focused nonprofit organizations '), ('government', 'Local, state, and federal government agencies and authorities'), ('philanthropy', 'Philanthropic organizations/Charitable foundations '), ('media', 'Media organizations'), ('student', 'Students'), ('researcher', 'Researchers'), ('mission_aligned_dev', 'Mission-aligned developers'), ('financial_inst', 'Financial Institutions')], max_length=64)),
                ('affiliation', models.CharField(blank=True, max_length=128, null=True)),
                ('intended_use', models.TextField(blank=True, null=True)),
                ('expected_account_tenure', models.IntegerField(default=4, help_text='in weeks')),
                ('conflicts', models.TextField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('agreed_to_terms', models.BooleanField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]