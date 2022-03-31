# Generated by Django 4.0.3 on 2022-03-31 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Running',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('temperature', models.IntegerField()),
                ('weather', models.CharField(choices=[('CL', 'ceu limpo'), ('PN', 'parcialmente nublado'), ('NU', 'nublado'), ('CH', 'chuva'), ('VE', 'ventania')], default='CL', max_length=2)),
                ('total_distance', models.FloatField()),
                ('running_start', models.DateTimeField()),
                ('running_end', models.DateTimeField()),
                ('elapsed_time', models.DurationField()),
                ('calories', models.IntegerField()),
                ('cadence', models.IntegerField()),
                ('elevation_gain', models.IntegerField()),
                ('elevation_loss', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km', models.FloatField()),
                ('avg_pace', models.DurationField()),
                ('elevation', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('running', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corridas.running')),
            ],
        ),
    ]
