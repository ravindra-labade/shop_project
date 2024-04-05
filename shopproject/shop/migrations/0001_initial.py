# Generated by Django 5.0.4 on 2024-04-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=20)),
                ('shop_address', models.CharField(max_length=20)),
                ('shop_owner', models.CharField(max_length=20)),
                ('operated_since', models.DateField()),
                ('available_services', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(choices=[('Online', 'ONLINE'), ('Cash', 'CASH')], max_length=10)),
            ],
        ),
    ]
