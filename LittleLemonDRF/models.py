from django.db import models

# Create your models here.
class AuthorDet(models.Model):
    gender = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.gender
    


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    authordet = models.ForeignKey(AuthorDet, on_delete = models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['price'])
        ]
    
    def __str__(self):
        return self.title
    


    
    