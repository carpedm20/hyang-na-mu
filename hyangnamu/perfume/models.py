from django.db import models

LONGEVITY = (
    (1, _("poor")),
    (2, _("weak")),
    (3, _("moderate")),
    (4, _("long")),
    (5, _("very long"))
)

SILLAGE = (
    (1, _("soft")),
    (2, _("moderate")),
    (3, _("heavy")),
    (4, _("enormous"))
)

STATUS = (
    (1, _("love")),
    (2, _("like")),
    (3, _("dislike")),
    (4, _("spring")),
    (5, _("summer")),
    (6, _("fall")),
    (7, _("winter")),
    (8, _("day")),
    (9, _("night")),
)

# Create your models here.
class Perfume(models.Model):
    name = models.CharField(max_length=200)

    brand = models.CharField(max_length=200)
    group = 
    date = models.DateField()
    pictures = models.CommaSeparatedIntegerField()
    description = models.charField(max_length = 1000)

    longevity = models.IntegerField(choices=LONGEVITY)
    sillage = models.IntegerField(choices=SILLAGE)
    status = models.IntegerField(choices=STATUS)

    shops = models.CommaSeparatedIntegerField()

    def __unicode(self):
        return "<Perfume %s (%s)>" % self.name, self.url

class Brand(models.Model):
    name = models.CharField(max_length = 100)
    url = models.URLField()
    country = models.URLField()
    company = 
    description = models.charField(max_length = 1000)

class Company(models.Model):
    name = models.charField(max_length = 50)

class Group(models.Model):
    name = models.charField(max_length = 50)
    description = models.charField(max_length = 1000)

