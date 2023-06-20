from django.contrib import admin

# Register your models here.

from .models  import Contactform, About, Projects, Contact, Social, Procent

admin.site.register(Contactform) 
admin.site.register(About)
admin.site.register(Projects)
admin.site.register(Contact)
admin.site.register(Social)
admin.site.register(Procent)