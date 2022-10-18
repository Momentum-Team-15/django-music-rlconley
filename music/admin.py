from django.contrib import admin
from .models import User, Album, Artist

# Register your models here, so you can see them in the admin.
admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)