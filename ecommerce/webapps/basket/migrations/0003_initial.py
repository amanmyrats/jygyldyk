# Generated by Django 3.2 on 2023-02-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basket', '0002_initial'),
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='vouchers',
            field=models.ManyToManyField(blank=True, to='voucher.Voucher', verbose_name='Vouchers'),
        ),
        migrations.AlterUniqueTogether(
            name='line',
            unique_together={('basket', 'line_reference')},
        ),
    ]