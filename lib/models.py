from django.db import models


class reader(models.Model):
    id = models.IntegerField()
    full_name = models.CharField()
    age = models.IntegerField()
    number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField()
    book = models.ForeignKey('book', on_delete=models.CASCADE)

    def __str__(self, full_name):
        return self.full_name


class book(models.Model):
    id = models.BigIntegerField()
    name = models.CharField()
    author = models.CharField()
    genre = models.CharField()
    amount = models.IntegerField()

    def __str__(self, name):
        return self.name