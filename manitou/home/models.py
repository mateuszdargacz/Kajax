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
    tags = models.CharField(max_length=128, blank=True, null=True)
    button_text = models.CharField(max_length=64, blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slider = Slider.objects.first()
        super(SliderImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.header


class Lifter(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def image(self):
        if not self.images.exists():
            return None
        image = self.images.filter(is_primary=True).first()
        if not image:
            image = self.images.first()
        return image.image.url


class LifterImage(models.Model):
    lifter = models.ForeignKey(Lifter, related_name='images')

    alt = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(upload_to='lifter/images/')
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk and self.is_primary and self.lifter.images.filter(is_primary=True).exclude(pk=self.pk).exists():
            # if changed to primary
            self.lifter.images.filter(is_primary=True).exclude(pk=self.pk).update(is_primary=False)
        elif not self.pk and self.is_primary:
            self.lifter.images.filter(is_primary=True).update(is_primary=False)

        super(LifterImage, self).save(*args, **kwargs)


class LifterFeature(models.Model):
    text = models.CharField(max_length=256)
    lifter = models.ForeignKey(Lifter, related_name='features')


class AddEquip(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    icon = models.ImageField(upload_to='add_equip/icons')
    order = models.IntegerField(unique=True)


class Message(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
