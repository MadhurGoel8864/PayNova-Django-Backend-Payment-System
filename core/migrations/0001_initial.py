# Generated by Django 3.2.7 on 2025-06-16 18:01

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=5, max_length=20, prefix='CARD', unique=True)),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('card_type', models.CharField(choices=[('master', 'master'), ('visa', 'visa'), ('verve', 'verve')], default='master', max_length=20)),
                ('card_status', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('None', 'None'), ('Transfer', 'Transfer'), ('Credit Alert', 'Credit Alert'), ('Debit Alert', 'Debit Alert'), ('Sent Payment Request', 'Sent Payment Request'), ('Recieved Payment Request', 'Recieved Payment Request'), ('Funded Credit Card', 'Funded Credit Card'), ('Withdrew Credit Card Funds', 'Withdrew Credit Card Funds'), ('Deleted Credit Card', 'Deleted Credit Card'), ('Added Credit Card', 'Added Credit Card')], default='none', max_length=100)),
                ('amount', models.IntegerField(default=0)),
                ('is_read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('nid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
            ],
            options={
                'verbose_name_plural': 'Notification',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=15, max_length=20, prefix='TRN', unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('failed', 'failed'), ('completed', 'completed'), ('pending', 'pending'), ('processing', 'processing'), ('request_sent', 'request_sent'), ('request_settled', 'request settled'), ('request_processing', 'request processing')], default='pending', max_length=100)),
                ('transaction_type', models.CharField(choices=[('transfer', 'Transfer'), ('recieved', 'Recieved'), ('withdraw', 'withdraw'), ('refund', 'Refund'), ('request', 'Payment Request'), ('none', 'None')], default='none', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
