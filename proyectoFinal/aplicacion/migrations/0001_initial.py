# Generated by Django 4.2.3 on 2023-08-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='direccionDeResidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('numeracion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='edad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaNacimiento', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='identificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='nombre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
    ]
