from django.db import models

# Create your models here.

class Schedule(models.Model):
    TERM = (
        ('Gasal 2019/2020', 'Gasal 2019/2020'),
        ('Genap 2019/2020', 'Genap 2019/2020'),
        ('Gasal 2020/2021', 'Gasal 2020/2021'),
        ('Genap 2020/2021', 'Genap 2020/2021'),
    )
    HARI = (
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'),
        ('Jumat', 'Jumat'),
    )
    matkul = models.CharField(max_length=100, null=True)
    sks = models.CharField(max_length=2, null=True)
    deskripsi = models.CharField(max_length=200, null=True)
    dosen = models.CharField(max_length=100, null=True)
    ruangan = models.CharField(max_length=100, null=True)
    term = models.CharField(max_length=100, null=True, choices=TERM)
    hari = models.CharField(max_length=10, null=True, choices=HARI, default='Senin')

    def __str__(self):
        return self.matkul