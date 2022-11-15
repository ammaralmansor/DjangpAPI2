from django.db import models 
from django.urls import reverse

# Create your models here.

# Two database models (Note, Author)
class Auther(models.Model):

    name = models.CharField(max_length=25)
    
    class Meta:
        verbose_name = ("Auther")
        verbose_name_plural = ("Authers")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Auther_detail", kwargs={"slug": self.slug})

        
class Note(models.Model):

    auther = models.ForeignKey("Auther", related_name='relationship' , on_delete=models.CASCADE)
    note = models.TextField(max_length=500)


    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return str(self.auther) + "_note" 

    # def get_absolute_url(self):
    #     return reverse("Note_detail", kwargs={"slug": self.slug})

