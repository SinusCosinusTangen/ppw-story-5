# Generated by Django 3.1.2 on 2020-10-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('sks', models.CharField(max_length=2, null=True)),
                ('deskripsi', models.CharField(max_length=200, null=True)),
                ('dosen', models.CharField(max_length=100, null=True)),
                ('ruangan', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
