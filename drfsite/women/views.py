from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


from .serializers import WomenSerializer
from rest_framework.decorators import action
from .models import Category, Women
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes =(IsAdminOrReadOnly,)  

