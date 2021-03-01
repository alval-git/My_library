from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
    	return self.full_name
class PublishHouse(models.Model):
    name  = models.TextField(default='без издательства')
    def __str__(self):
        return self.name
class Friend(models.Model):
    name = models.TextField(default='имя')
    def __str__(self):
        return self.name


class book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=9,default=0)
    publish_house = models.ForeignKey(PublishHouse, on_delete=models.SET_DEFAULT , default=1)
    image = models.ImageField(upload_to='books_image/', blank=True)
    def __str__(self):
    	return self.title
    

class WhoAndWhatTook(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    def __str__(self):
        	return "{} взял {}".format(self.friend,self.book)





