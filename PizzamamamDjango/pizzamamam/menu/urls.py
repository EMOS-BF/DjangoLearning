from . import views
from django.urls import path
app_name ="menu"
urlpatterns = [
    path('', views.index, name="index"),
]