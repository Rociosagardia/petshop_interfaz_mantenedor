# Generated by Django 3.2.4 on 2021-06-26 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210625_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='nombreMarca',
            field=models.CharField(max_length=200, verbose_name='nombre de Marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.marca'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
    ]