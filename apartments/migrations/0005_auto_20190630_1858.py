# Generated by Django 2.2.2 on 2019-06-30 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_auto_20190630_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Address', unique=True),
        ),
    ]
