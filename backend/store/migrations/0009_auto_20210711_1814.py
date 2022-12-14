# Generated by Django 3.2.3 on 2021-07-11 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_friend'),
        ('store', '0008_auto_20210707_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_active',
            new_name='is_available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='regular_price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.99, error_messages={'name': {'max_length': 'The price must be between 0 and 999,999.99.'}}, help_text='Maximum 999,999.99', max_digits=8, verbose_name='Price'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites', models.ManyToManyField(related_name='favorites', to='store.Product')),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='vendor.vendor')),
            ],
        ),
    ]
