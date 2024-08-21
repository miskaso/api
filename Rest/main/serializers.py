from rest_framework import serializers
from .models import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'

    def validate_name(self, value):
        if value[0].isdigit():
            raise serializers.ValidationError("Название не может начинаться с цифр.")
        elif value.isalnum() and len(value.strip()) != 0:
            return value
        else:
            raise serializers.ValidationError("Ошибка! Что-то пошло не так.")

    def validate_country(self, value):
        country = ['Kyrgyzstan', 'Germany']
        if value not in country:
            raise serializers.ValidationError("Ошибка! Недопустимая страна.")
        return value

    def validate_info(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError("Ошибка! Слишком мало информации о машине.")
        return value
