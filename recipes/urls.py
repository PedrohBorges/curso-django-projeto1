from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/category/<int:category_id>/', views.category, name="recipes-category"),
    path('recipes/<int:id>/', views.recipes, name="recipes-recipe"),
    path('admin/', admin.site.urls),
]
