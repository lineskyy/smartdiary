from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    start_time = models.DateTimeField(null=True , blank=True)
    end_time = models.DateTimeField(null=True , blank=True)
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'