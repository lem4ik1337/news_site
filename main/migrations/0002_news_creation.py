# Generated by Django 5.0 on 2024-01-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='creation',
            field=models.CharField(max_length=50, null=True, verbose_name='Создатель'),
        ),
    ]
