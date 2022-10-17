from django.urls import path

# importing views from views..py
from .views import eliminar_usuario, index

urlpatterns = [
    path('', index, name="pagina_principal"),
    path('<id>/eliminar', eliminar_usuario, name="delete_person"),
]
