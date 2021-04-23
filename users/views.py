from rest_framework import viewsets
from .serializers import PersonSerializer,models
# Create your views here.


class PersonAPIView(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = PersonSerializer
