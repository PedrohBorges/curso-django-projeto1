from . import views
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/', views.category, name="recipes-category"), # noqa 501
    path('recipe/<int:id>/', views.recipe, name="recipes-recipe"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
