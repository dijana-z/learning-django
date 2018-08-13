from django.contrib import admin
# importing our models
from .models import Album, Song

# register the imported models on admin site (they will appear on url ".../admin")
admin.site.register(Album)
admin.site.register(Song)

