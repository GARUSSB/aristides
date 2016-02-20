from django.conf.urls import url
from django.contrib import admin
from control.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crear_personal/', crear_personal),
    url(r'^editar_personal/', editar_personal),
    url(r'^get_all_personal/', get_all_personal),
    url(r'^get_personal/', get_personal),
    url(r'^crear_inacistencia/', crear_inacistencia),
    url(r'^editar_inacistencia/', editar_inacistencia),
    url(r'^get_all_inacistencia/', get_all_inacistencia),
    url(r'^get_personal_inacistencia/', get_personal_inacistencia),
    url(r'^$', index.as_view(), name= "index"),
]
