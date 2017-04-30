# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewTest', '0003_auto_20170429_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gebruiker', models.IntegerField()),
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
                ('id_adress', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_gebruiker', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Producten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=555)),
            ],
        ),
        migrations.DeleteModel(
            name='LinkMenuCategorie',
        ),
        migrations.DeleteModel(
            name='NavigatieMenu',
        ),
        migrations.AddField(
            model_name='product',
            name='btwPercentage',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.CharField(default='dit is een test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='voorraad',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]