from django.db import models

# Create your models here.
class task(models.Model):
    Title = models.CharField(max_length=255)
    Done = models.BooleanField(default=False)
    Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if (self.Done):
            return f'{self.Title}: Done'
        else:
            return f'{self.Title}: Active'