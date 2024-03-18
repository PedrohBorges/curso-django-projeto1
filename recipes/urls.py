from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('admin/', admin.site.urls),
]
