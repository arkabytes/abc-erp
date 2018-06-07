# Generated by Django 2.0.3 on 2018-06-07 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ABC', '0041_auto_20180207_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Customer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Provider'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Order'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.PaymentType'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Invoice'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Provider'),
        ),
        migrations.AlterField(
            model_name='item',
            name='vat_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.VatType'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.DeliveryType'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.PaymentType'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Item'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Order'),
        ),
        migrations.AlterField(
            model_name='task',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Customer'),
        ),
        migrations.AlterField(
            model_name='task',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Order'),
        ),
        migrations.AlterField(
            model_name='task',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ABC.Provider'),
        ),
    ]
