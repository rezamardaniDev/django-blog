from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
        ('disable', 'DISABLE')
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    post_view = models.IntegerField(default=0, editable=False)
    
    
    def __str__(self):
        return self.title
    