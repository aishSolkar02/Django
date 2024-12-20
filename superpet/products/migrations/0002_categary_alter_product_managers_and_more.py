# Generated by Django 5.1.1 on 2024-10-21 04:45

import autoslug.fields
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categary_name', models.CharField(max_length=100)),
                ('categary_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='categary_name', unique=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('customManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(default='superpet', max_length=100),
        ),
    ]
