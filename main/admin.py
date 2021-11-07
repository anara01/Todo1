from django.contrib import admin

# Register your models here.
from .models import ToDo

from .models import ToMeet

admin.site.register(ToDo)

admin.site.register(ToMeet)
