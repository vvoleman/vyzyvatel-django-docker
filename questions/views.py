from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from .models import Category, Question
from .serializers import *
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def GetCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def DrawQuestions(request):
    #categories_names = request.data.get('categories')
    #number_of_questions = request.data.get('questions')

    categories_names = ['Historie']

    questions = []

    if categories_names:
        for category_name in categories_names:
            category = Category.objects.filter(name=category_name)
            questions = questions + list(category[0].question_set.all())

        serializer = QuestionSerializer(questions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_404_NOT_FOUND)
