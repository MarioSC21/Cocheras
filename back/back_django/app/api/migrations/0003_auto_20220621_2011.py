# Generated by Django 3.2 on 2022-06-22 01:11

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220620_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cochera',
            name='imagen1',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dyg8vlnnz/image/upload/v1655859589/duciogqgpxvbidt0dcpj.jpg', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='cochera',
            name='imagen2',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dyg8vlnnz/image/upload/v1655859589/duciogqgpxvbidt0dcpj.jpg', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='cochera',
            name='imagen3',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dyg8vlnnz/image/upload/v1655859589/duciogqgpxvbidt0dcpj.jpg', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='cochera',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]