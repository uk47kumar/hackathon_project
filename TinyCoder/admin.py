from django.contrib import admin

from TinyCoder.models import Contact, SIGNUP, LOGIN, APPOINTMENT
# Register your models here.

admin.site.register(Contact)
admin.site.register(SIGNUP)
admin.site.register(LOGIN)
admin.site.register(APPOINTMENT)
