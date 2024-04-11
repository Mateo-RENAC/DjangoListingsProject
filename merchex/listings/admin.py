from django.contrib import admin

from listings.models import Band, LISTINGS

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class LISTINGSAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'band', 'year')

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(LISTINGS, LISTINGSAdmin)

