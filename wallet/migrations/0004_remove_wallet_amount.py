# Generated by Django 4.0.6 on 2022-08-02 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_alter_account_account_type_alter_customer_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='amount',
        ),
    ]
