# Generated by Django 3.2.13 on 2022-11-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_ntsc'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='AdobeRGB',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='DPAltMode',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='GPU기술',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='리프트힌지',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='전용펜지원',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='침수지연키보드',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='NTSC',
            field=models.TextField(blank=True, null=True),
        ),
    ]
