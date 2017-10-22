from django.contrib import admin

from .models import Municipality, ONG,UserProfile
admin.site.register(UserProfile)
admin.site.register(Municipality)
admin.site.register(ONG)
