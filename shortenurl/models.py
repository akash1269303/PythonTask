from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings
# Create your models here.



class Link(models.Model):
    original_url=models.URLField()
    shorten_url=models.URLField(blank=True,null=True)


    # Logic For Creating Shorten Url 
    def shortener(self):
        while True:
            random_string=''.join(choices(ascii_letters,k=6))
            new_link=settings.HOST_URL+'/'+random_string 
            if not Link.objects.filter(shorten_url=new_link).exists():
                 break
        return new_link


    def save(self,*args, **kwargs):
        if not self.shorten_url:
            new_link=self.shortener()
            self.shorten_url=new_link
        return super().save(*args, **kwargs)
