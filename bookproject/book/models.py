from django.db import models



class Book(models.Model):
    book_name = models.CharField(max_length=10)
    author_name = models.CharField(max_length=20)
    publication = models.CharField(max_length=20)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
    choice = [('Online', 'ONLINE'), ('Cash', 'Cash On Delivery')]
    payment_mode = models.CharField(max_length=10, choices=choice)
