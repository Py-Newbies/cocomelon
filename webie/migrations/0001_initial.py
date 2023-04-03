# Generated by Django 4.1.7 on 2023-04-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
    ]
