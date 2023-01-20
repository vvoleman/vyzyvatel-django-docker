from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def Authentication(request):
    response = {
        "username": request.user.username,
        "email": request.user.email
    }
    return Response(response, status=status.HTTP_200_OK)
