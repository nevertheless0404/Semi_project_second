# Generated by Django 3.2.13 on 2022-11-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_comments_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('잡담', '잡담'), ('질문', '질문'), ('자랑', '자랑'), ('고민/상담', '고민/상담'), ('인사', '인사')], max_length=50),
        ),
    ]
