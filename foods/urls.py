from django.urls import path, include
from .views import FoodCategoryListAPIView

urlpatterns = [
    path("foods/", FoodCategoryListAPIView.as_view()),
]
