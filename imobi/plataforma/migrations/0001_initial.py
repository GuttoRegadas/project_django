# Generated by Django 4.0.2 on 2022-02-17 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DiasVisita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Imovei',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('quartos', models.IntegerField()),
                ('tamanho', models.FloatField()),
                ('rua', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('V', 'Venda'), ('A', 'Aluguel')], max_length=1)),
                ('tipo_imovel', models.CharField(choices=[('A', 'Apartamento'), ('C', 'Casa')], max_length=1)),
                ('numero', models.IntegerField()),
                ('descricao', models.TextField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plataforma.cidade')),
                ('dias_visita', models.ManyToManyField(to='plataforma.DiasVisita')),
                ('horarios', models.ManyToManyField(to='plataforma.Horario')),
                ('imagens', models.ManyToManyField(to='plataforma.Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=20)),
                ('horario', models.TimeField()),
                ('status', models.CharField(choices=[('A', 'Agendado'), ('F', 'Finalizado'), ('C', 'Cancelado')], default='A', max_length=1)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plataforma.imovei')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
