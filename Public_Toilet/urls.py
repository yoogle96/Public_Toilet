from django.contrib import admin
from django.urls import path
import Toilet_Map.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', Toilet_Map.views.home, name="home"),
    path('test/', Toilet_Map.views.test, name="test"),
]
