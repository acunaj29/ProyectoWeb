from django.urls import path
from .views import VRegistro

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',VRegistro.as_view(),  name="autenticacion"),
]