# Generated by Django 3.1.2 on 2020-10-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_story5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='term',
            field=models.CharField(choices=[('Gasal 2019/2020', 'Gasal 2019/2020'), ('Genap 2019/2020', 'Genap 2019/2020'), ('Gasal 2020/2021', 'Gasal 2020/2021'), ('Genap 2020/2021', 'Genap 2020/2021')], max_length=100, null=True),
        ),
    ]
