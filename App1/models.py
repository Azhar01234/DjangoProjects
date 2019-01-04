from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} {self.code}"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
                     # ^ this points to Airport Class above. ^this will delete all the flights if airport is deleted.
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()	
    def __str__(self): #this is a magic method which defines the class in a more meaningfull manner 
        return f"{self.id} - {self.origin} to {self.destination}"
                  #^ id is automatically created by django in database in fiel migrations
