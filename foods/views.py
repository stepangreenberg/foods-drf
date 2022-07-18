from django.db.models import Prefetch, Count

from .serializers import FoodListSerializer
from rest_framework import generics
from .models import Food, FoodCategory


class FoodCategoryListAPIView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        food_category_queryset = (
            FoodCategory.objects

            # Фильтруем категории (если нет опубликованной еды - не выводим категорию)
            .filter(food__is_publish=True)
            .annotate(food_published_count=Count("food"))
            .filter(food_published_count__gte=0)

            # Фильтруем опубликованную еду (если еда не опубликована - не выводим)
            # Результат заносим в food_filtered для вывода через FoodListSerializer
            .prefetch_related(
                Prefetch(
                    "food",
                    queryset=Food.objects.filter(is_publish=True),
                    to_attr="food_filtered",
                )
            )
        )

        return food_category_queryset
