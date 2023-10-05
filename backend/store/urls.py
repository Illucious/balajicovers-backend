from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("categories/", views.categories, name="categories"),
    path("subcategories/<str:fk>/", views.subcategories, name="subcategories"),
]
