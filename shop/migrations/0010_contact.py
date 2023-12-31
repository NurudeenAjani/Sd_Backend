# Generated by Django 4.1.4 on 2023-06-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_cart_cartitem_rename_product_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
