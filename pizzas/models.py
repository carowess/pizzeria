from django.db import models

# Create your models here.

class Pizza(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # This is how it know to return the text field 
    # instead of saying "Pizza_object(1)"
    def __str__(self):
        return self.text

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    # This is how it know to return the text field 
    # instead of saying "Topping_object(1)"
    def __str__(self):
        return self.name
