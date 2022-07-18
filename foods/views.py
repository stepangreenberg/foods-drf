from django.db.models import Prefetch, Count

from .serializers import FoodListSerializer
from rest_framework import generics
from .models import Food, FoodCategory


class FoodCategoryListAPIView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        food_category_queryset = (
            FoodCategory.objects.prefetch_related(
                Prefetch(
                    "food",
                    queryset=Food.objects.filter(is_publish=True),
                    to_attr="filtered_food",
                )
            )
            .filter(food__is_publish=True)
            .annotate(publish_count=Count("food"))
            .filter(publish_count__gte=0)
        )

        return food_category_queryset
