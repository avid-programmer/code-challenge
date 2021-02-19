from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CustomerSerializer

@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            customer = serializer.save()
            data['response'] = "Successfully registered a new user"
        else:
            data = serializer.errors
        return Response(data)

