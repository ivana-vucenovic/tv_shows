from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) < 10:
            if len(postData['description']) == 0:
                pass
            else:
                errors["description"] = "Description should be at least 10 characters"

        return errors

class Show(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    network = models.CharField(max_length = 255)
    description = models.CharField(max_length= 255)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
    

