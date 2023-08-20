from django.db import models

# Create your models 

class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    activate = models.BooleanField(default=True)
    
    def _str_(self):
        return self.name()