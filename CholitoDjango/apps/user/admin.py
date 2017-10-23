from django.contrib import admin


from .models import Municipality, ONG, TypeUser

admin.site.register(Municipality)
admin.site.register(ONG)
admin.site.register(TypeUser)
