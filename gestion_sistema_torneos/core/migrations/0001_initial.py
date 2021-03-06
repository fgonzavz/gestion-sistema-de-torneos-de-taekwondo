# Generated by Django 2.2.6 on 2019-12-03 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('grado', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('ciudad', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('grado', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=25)),
                ('competidores_participantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Competidores')),
                ('equipo_participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='maestro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Maestro'),
        ),
        migrations.AddField(
            model_name='competidores',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipo'),
        ),
    ]
