from django.db import models

class Food(models.Model):
    name = models.CharField(max_length = 50);
    picture = models.ImageField(null = True);

    def __str__(self):
        return self.name;
    
class Type(models.Model):
    type = models.CharField(max_length = 30);

    def __str__(self):
        return self.type;
    
    
class Town(models.Model):
    name = models.CharField(max_length = 50);
    picture = models.ImageField(upload_to = 'images/', null = True, blank = True)
    def __str__(self):
        return self.name;
    
class Restaurant(models.Model):
    name = models.CharField(max_length = 30);
    phone = models.CharField(max_length = 12);
    address = models.CharField(max_length = 100);
    food = models.ForeignKey(Food);
    town = models.ForeignKey(Town);
    cost = models.CharField(max_length = 20);
    restaurant_type = models.ForeignKey(Type);
    menu = models.ImageField(upload_to = 'images/', null = True, blank = True );
    map = models.ImageField(upload_to = 'images/', null = True, blank = True);
    picture = models.ImageField(upload_to = 'images/', null = True, blank = True);

    STARS = ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),);
    votes = models.IntegerField(choices = STARS, default = 4);

    def __str__(self):
        return self.name;
    

# Create your models here.
