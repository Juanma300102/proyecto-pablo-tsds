from django.db import models


class Course(models.Model):
    year = models.PositiveIntegerField()
    divition = models.CharField(max_length=1)

    def __str__(self) -> str:
        return f"{self.year}{self.divition}"


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    birth = models.DateField()
    adress = models.CharField(max_length=255)
    course = models.OneToOneField(Course, models.RESTRICT)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
