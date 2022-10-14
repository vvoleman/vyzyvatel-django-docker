from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def GetEmail(request):
    return Response(request.user.email, status=status.HTTP_200_OK)
