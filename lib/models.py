from django.db import models


class reader(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    number = models.IntegerField()
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250)
    book = models.ForeignKey('book', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    amount = models.IntegerField()

    def __str__(self):
        return self.name