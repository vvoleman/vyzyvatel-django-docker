from rest_framework import serializers

from .models import Category, PickQuestion, NumericQuestion


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class PickQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickQuestion
        fields = ("id", "question",
                  "right_answer", "wrong_answers")


class NumericQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericQuestion
        fields = ("id", "question", "right_answer")
