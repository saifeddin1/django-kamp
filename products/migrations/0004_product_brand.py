# Generated by Django 3.0.7 on 2020-07-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200707_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='brand', max_length=100),
            preserve_default=False,
        ),
    ]