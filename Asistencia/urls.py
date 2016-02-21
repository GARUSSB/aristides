from django.conf.urls import url
from django.contrib import admin
from control.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crear_personal/', crear_personal),
    url(r'^crear_cargos/', crear_cargos),
    url(r'^drop_cargos/', delete_cargo),
    url(r'^editar_personal/', editar_personal),
    url(r'^get_all_personal/', get_all_personal),
    url(r'^get_personal/', get_personal),
    url(r'^get_cargos/', get_cargos),
    url(r'^edit_cargos/', edit_cargos),
    url(r'^crear_inacistencia/', crear_inacistencia),
    url(r'^get_all_inacistencia/', get_all_inacistencia),
    url(r'^get_personal_inacistencia/', get_personal_inacistencia),
    url(r'^$', index.as_view(), name= "index"),
]
