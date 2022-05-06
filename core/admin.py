from django.contrib import admin
from core.models import *

# Register your models here.

RegisteredModels = [
    Person
]

admin.site.register(RegisteredModels)
