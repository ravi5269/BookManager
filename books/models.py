from django.db import models

# Create your models here

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title
