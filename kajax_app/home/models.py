from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.id = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass



class CompanyData(SingletonModel):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=512)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Slider(SingletonModel):
    name = models.CharField(max_length=128)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    header = models.CharField(max_length=128)
    image = models.ImageField(upload_to='slider/images')
    short_desc = models.CharField(max_length=256, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    slider = models.ForeignKey(Slider, related_name='images')

    def __str__(self):
        return self.header


class Service(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=128)
    desc = models.TextField()
    image = models.ImageField(upload_to='services/images')


    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField()
    image = models.ImageField(upload_to='client/images')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128)
    short_desc = models.CharField(max_length=256)
    desc = models.TextField()

    # Project facts
    project_start = models.DateField(null=True, blank=True)
    project_end = models.DateField(null=True, blank=True)
    client = models.ForeignKey(Client, related_name='projects')
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    name = models.CharField(max_length=56)
    primary = models.BooleanField(default=False)
    image = models.ImageField(upload_to='projects/images')
    project = models.ForeignKey(Project, related_name='images')

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
