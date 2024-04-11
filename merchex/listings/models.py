from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
# Create your models here.

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        KPOP = 'KP'
        JPOP = 'JP'
        OTHER = 'OT'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024), ])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class LISTINGS(models.Model):

    class ListingType(models.TextChoices):
        RECORD = 'R'
        CLOTHING = 'C'
        POSTER = 'P'
        MISC = 'M'



    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null = True, validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)