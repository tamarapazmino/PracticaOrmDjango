# Generated by Django 3.0.7 on 2020-08-02 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOrm', '0002_auto_20200730_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appOrm.Cliente'),
        ),
    ]