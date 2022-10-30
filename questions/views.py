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
    active_categories_id = request.data.get('categories')
    print(active_categories_id)

    categories = Category.objects.filter(pk__in=active_categories_id)
    print(categories)

    pick_questions = []
    numeric_questions = []
    for category in categories:
        pick_questions = pick_questions + list(category.pickquestion_set.all())
        numeric_questions = numeric_questions + \
            list(category.numericquestion_set.all())

    random.shuffle(pick_questions)
    random.shuffle(numeric_questions)

    pick_question_serializer = PickQuestionSerializer(
        pick_questions[0:3], many=True)
    numeric_question_serializer = NumericQuestionSerializer(
        numeric_questions[0:3], many=True)

    return Response({"pickQuestions": pick_question_serializer.data,
                     "numericQuestions": numeric_question_serializer.data}, status=status.HTTP_404_NOT_FOUND)
