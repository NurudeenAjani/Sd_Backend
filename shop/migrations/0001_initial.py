# Generated by Django 4.1.4 on 2023-06-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=14)),
                ('description', models.TextField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
