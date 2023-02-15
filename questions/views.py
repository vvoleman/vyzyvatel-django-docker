from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from .models import Category, PickQuestion, NumericQuestion
from .serializers import *
from rest_framework.permissions import IsAuthenticated
import random
from django.core import serializers


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def GetCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def DrawQuestions(request):
    try:
        active_categories_id = request.data.get('categories')

        categories = Category.objects.filter(pk__in=active_categories_id)

        pick_questions = []
        numeric_questions = []
        image_questions = []
        for category in categories:
            pick_questions += list(category.pickquestion_set.all())
            numeric_questions += list(category.numericquestion_set.all())
            image_questions += list(category.imagequestion_set.all())

            category.popularity += 1
            category.save()

        random.shuffle(pick_questions)
        random.shuffle(numeric_questions)
        random.shuffle(image_questions)

        pick_question_serialized = PickQuestionSerializer(
            pick_questions[0:12], many=True)
        numeric_question_serialized = NumericQuestionSerializer(
            numeric_questions[0:16], many=True)
        image_question_serialized = ImageQuestionSerializer(
            image_questions[0:12], many=True)

        return Response({"pickQuestions": pick_question_serialized.data,
                        "numericQuestions": numeric_question_serialized.data,
                         "imageQuestions": image_question_serialized.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
