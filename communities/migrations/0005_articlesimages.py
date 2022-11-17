# Generated by Django 3.2.13 on 2022-11-17 02:07

import communities.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_merge_20221117_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=communities.models.get_image_filename)),
                ('articles', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articles_image', to='communities.articles')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
