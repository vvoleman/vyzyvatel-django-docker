from rest_framework import serializers
from .models import Category, PickQuestion, NumericQuestion, ImageQuestion


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class PickQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickQuestion
        fields = ("id", "question",
                  "right_answer", "wrong_answers", "get_category")


class NumericQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericQuestion
        fields = ("id", "question", "right_answer", "get_category")


class ImageQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageQuestion
        fields = ("id", "image_url", "question",
                  "right_answer", "wrong_answers", "get_category")
