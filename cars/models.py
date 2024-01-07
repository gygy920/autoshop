from django.db import models


# Create your models here.
class Mark(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} - {self.country}'


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=30)
    is_dark = models.BooleanField

    def __str__(self):
        return self.name


class Car(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    year = models.IntegerField(default=2000)
    model = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.model} - {self.color} - {self.year} - {self.type} - {self.mark}'



