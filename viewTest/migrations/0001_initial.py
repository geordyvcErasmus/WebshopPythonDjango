# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gebruiker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wachtwoord', models.CharField(max_length=255)),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Adress')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Producten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Merk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('voorraad', models.IntegerField()),
                ('btwPercentage', models.IntegerField()),
                ('summary', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='static/productimages/')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Categorie')),
                ('merk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Merk')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtext', models.TextField(max_length=555)),
            ],
        ),
        migrations.AddField(
            model_name='invoice_producten',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Product'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_producten',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Invoice_Producten'),
        ),
        migrations.AddField(
            model_name='gebruiker',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Invoice'),
        ),
        migrations.AddField(
            model_name='gebruiker',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewTest.Review'),
        ),
    ]
