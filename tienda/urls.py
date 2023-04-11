from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.tienda, name="tienda"),
    #path('contacto/', contacto,  name="contacto"),
]