from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)



class AboutAdmin(admin.ModelAdmin):
    list_display = ('age', 'birthday', 'phone', 'email', 'city')
    search_fields = ('email', 'city')

admin.site.register(About, AboutAdmin)




