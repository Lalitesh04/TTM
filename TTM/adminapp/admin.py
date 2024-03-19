from django.contrib import admin
from .models import Admin, Register, Packages

# Register your models here.

admin.site.register(Admin)
admin.site.register(Register)
admin.site.register(Packages)
