from rest_framework import serializers

from .models import Category, Question


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "get_category", "get_type", "question", "answers")
