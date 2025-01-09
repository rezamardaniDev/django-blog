from django.db import models

# Create your models here.
class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    ]
     
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Title: {self.title} | Status: {self.status}"