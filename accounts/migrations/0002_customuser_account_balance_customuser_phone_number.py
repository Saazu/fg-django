# Generated by Django 4.0.10 on 2024-05-27 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='account_balance',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_balanace', to='accounts.accountbalance'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_number', to='accounts.phonenumber'),
        ),
    ]
