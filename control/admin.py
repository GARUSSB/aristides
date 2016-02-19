from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import *


admin.site.register(Personal)
admin.site.register(Inacistencia)
admin.site.register(Cargo)