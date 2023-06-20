from django.db import models



class Contactform(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    birthday = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    PhEmailone = models.EmailField()

class  Projects(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="media/img/%y")
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Contact(models.Model):
    Location = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Call = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.Location

class Social(models.Model):
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)


class Procent(models.Model):
    HTML = models.CharField(max_length=50)
    CSS = models.CharField(max_length=50)
    JAVASCRIPT = models.CharField(max_length=50)
    PYTHON = models.CharField(max_length=50)
    DJANGO = models.CharField(max_length=50)

