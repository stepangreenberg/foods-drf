from rest_framework import serializers
from .models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="internal_code"
    )

    class Meta:
        model = Food
        fields = (
            "internal_code",
            "code",
            "name_ru",
            "description_ru",
            "description_en",
            "description_ch",
            "is_vegan",
            "is_special",
            "cost",
            "additional",
        )


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # data = data.filter(user=self.context["request"].user, edition__hide=False)
        # data[0].filtered_food
        # data = data.filter(filtered_food__isnull=True)
        return super(FilteredListSerializer, self).to_representation(data)


class FoodListSerializer(serializers.ModelSerializer):
    filtered_f = FoodSerializer(source="filtered_food", many=True, read_only=True)

    class Meta:
        model = FoodCategory
        list_serializer_class = FilteredListSerializer
        fields = (
            "id",
            "name_ru",
            "name_en",
            "name_ch",
            "order_id",
            "filtered_f",
        )
