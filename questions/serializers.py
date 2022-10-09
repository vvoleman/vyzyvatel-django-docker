from rest_framework import serializers

from .models import Category, Question


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "category", "is_numeric", "question",
                  "right_answer", "wrong_answer1", "wrong_answer2", "wrong_answer3")
