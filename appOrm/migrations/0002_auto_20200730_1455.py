# Generated by Django 3.0.8 on 2020-07-30 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOrm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='appOrm.Cliente'),
        ),
    ]