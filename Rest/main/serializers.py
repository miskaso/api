from rest_framework import serializers
from .models import CarBrand, Book, Author, Profile
from django.contrib.auth.models import User


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


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    def create(self, validated_data):
        datas = validated_data.pop('books')
        author = Author.objects.create(**validated_data)

        for data in datas:
            Book.objects.create(author=author, **data)

        return author


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = User.objects.create(**validated_data)

        Profile.objects.create(name=user, **profile)

        return user
