# Generated by Django 3.2.16 on 2023-01-31 12:58

import core.utils
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import models_custom.fields.autoslugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(default=core.utils.get_default_currency, max_length=12, verbose_name='Currency')),
                ('amount_allocated', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Amount Allocated')),
                ('amount_debited', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Amount Debited')),
                ('amount_refunded', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Amount Refunded')),
                ('reference', models.CharField(blank=True, max_length=255, verbose_name='Reference')),
                ('label', models.CharField(blank=True, max_length=128, verbose_name='Label')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='order.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='Name')),
                ('code', models_custom.fields.autoslugfield.AutoSlugField(blank=True, editable=False, help_text='This is used within forms to identify this source type', max_length=128, populate_from='name', unique=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Source Type',
                'verbose_name_plural': 'Source Types',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txn_type', models.CharField(blank=True, max_length=128, verbose_name='Type')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')),
                ('reference', models.CharField(blank=True, max_length=128, verbose_name='Reference')),
                ('status', models.CharField(blank=True, max_length=128, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date Created')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='payment.source', verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ['-date_created'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='source',
            name='source_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='payment.sourcetype', verbose_name='Source Type'),
        ),
        migrations.CreateModel(
            name='Bankcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=128, verbose_name='Card Type')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('number', models.CharField(max_length=32, verbose_name='Number')),
                ('expiry_date', models.DateField(verbose_name='Expiry Date')),
                ('partner_reference', models.CharField(blank=True, max_length=255, verbose_name='Partner Reference')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankcards', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Bankcard',
                'verbose_name_plural': 'Bankcards',
                'abstract': False,
            },
        ),
    ]
