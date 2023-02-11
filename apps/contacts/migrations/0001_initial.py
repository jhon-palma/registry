# Generated by Django 4.1.5 on 2023-02-07 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('type_document', models.CharField(choices=[('', '---------'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('CC', 'Cedula de Ciudadanía'), ('CE', 'Cedula de Extranjería')], max_length=2)),
                ('document', models.CharField(max_length=12, unique=True)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('', '---------'), ('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('cellphone', models.CharField(blank=True, max_length=15)),
                ('ocupation', models.CharField(choices=[('', '---------'), ('Ama de Casa', 'Ama de Casa'), ('Buscando Trabajo', 'Buscando Trabajo'), ('Empleado privado', 'Empleado privado'), ('Empleado público', 'Empleado público'), ('Trabajador Independiente', 'Trabajador Independiente')], max_length=24)),
                ('skills', models.CharField(choices=[('', '---------'), ('primaria', 'Primaria'), ('secundaria', 'Secundaria'), ('profesional', 'Profesional'), ('postgrado', 'Postgrado'), ('maestría', 'Maestría')], max_length=11)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Urbanization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urbanization', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='UrbanizationLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaders', to='contacts.contacts')),
                ('urbanization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urbanizations', to='contacts.urbanization')),
            ],
        ),
        migrations.AddField(
            model_name='contacts',
            name='leader',
            field=models.ManyToManyField(blank=True, related_name='urbanization_leader', through='contacts.UrbanizationLeader', to='contacts.urbanization'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='urbanization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.urbanization'),
        ),
    ]
