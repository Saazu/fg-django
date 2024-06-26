# Generated by Django 4.0.10 on 2024-05-27 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_account_balance_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_balance',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='account_balanace', to='accounts.accountbalance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='phone_number', to='accounts.phonenumber'),
            preserve_default=False,
        ),
    ]
