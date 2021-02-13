from django.db import models
from django.utils import timezone
from agents.models import Agent
# Create your models here.
class Listening(models.Model):
    STATUS_CHOICES = (
        ('rent', 'Rent'),
        ('sale', 'Sale'),
    )
    agent = models.ForeignKey(Agent,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True,db_index=True)
    image = models.ImageField(upload_to='listings/%Y/%m/%d',blank=True)
    image2 = models.ImageField(upload_to='listings/%Y/%m/%d',blank=True)
    image3 = models.ImageField(upload_to='listings/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(null=False,max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.CharField(max_length=200)
    kitchen = models.IntegerField()
    garage = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing_detail',args=[str(self.slug)])

class Quickcontact(models.Model):
    email = models.EmailField()
    textarea = models.TextField(max_length=200)
    
    def __str__(self):
        return self.email


class AgentContact(models.Model):
    agentname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_subject = models.TextField(max_length=200)

    def __str__(self):
        return self.user_name
    