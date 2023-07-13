from django.urls import path
from api.v1.category.views import CategoryView
from api.v1.product.views import ProductView
from api.v1.subcategory.views import SubcategoryView


urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("category/<int:pk>/", CategoryView.as_view()),

    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductView.as_view()),

    path("subcategory/", SubcategoryView.as_view()),
    path("subcategory/<int:pk>/", SubcategoryView.as_view()),
]

