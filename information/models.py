from django.db import models

class Intro(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    email = models.EmailField()
    freelance = models.BooleanField(default=False)
    python = models.IntegerField()
    django = models.IntegerField()
    html = models.IntegerField()
    css = models.IntegerField()
    js = models.IntegerField()
    github = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return self.name
    