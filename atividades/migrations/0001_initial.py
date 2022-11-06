# Generated by Django 4.0.2 on 2022-02-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_id', models.CharField(max_length=20)),
                ('duracao', models.CharField(max_length=20)),
                ('lugar', models.CharField(max_length=100)),
                ('obs', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'atividade',
            },
        ),
    ]