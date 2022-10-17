from django.urls import path

# importing views from views..py
from .views import home, inicio, tabla

urlpatterns = [
    path('', inicio, name="index"),
    path('home', home, name="home"),
    path('tabla', tabla, name="tabla")

]
