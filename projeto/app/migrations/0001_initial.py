# Generated by Django 4.2.4 on 2023-08-22 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_acesso', models.DateTimeField(auto_now=True)),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pagina')),
            ],
        ),
        migrations.AddField(
            model_name='pagina',
            name='topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico'),
        ),
    ]
