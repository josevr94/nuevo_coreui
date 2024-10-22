# Generated by Django 4.2.9 on 2024-10-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_apertura', models.DateTimeField(auto_now_add=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, null=True)),
                ('abierta', models.BooleanField(default=True)),
                ('total_efectivo_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_efectivo_final', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
