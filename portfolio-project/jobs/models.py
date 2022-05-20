from django.db import models

# Create your models here. Model is a python class that can be saved into the database.
class Job(models.Model):
    # Image property to save an image with a type of ImageField, this field saves images of all types.
    image = models.ImageField(upload_to='images/')

    # Summary section with a type field of Characters of max length of 200
    summary = models.CharField(max_length=200)

    # Using summary field to describe the jobs
    def __str__(self):
        return self.summary
        
