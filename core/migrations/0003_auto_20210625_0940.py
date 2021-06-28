# Generated by Django 3.2.4 on 2021-06-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210625_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='SKU'),
        ),
    ]