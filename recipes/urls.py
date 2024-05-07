from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/category/<int:category_id>/', views.category, name="recipes-category"),
    path('recipe/<int:id>/', views.recipe, name="recipes-recipe"),
    path('recipes/search/', lambda request: ..., name="search"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
