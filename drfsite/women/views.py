from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .serializers import WomenSerializer
from .models import Women
from rest_framework.response import Response 


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# Чтение (по GET-запросу) и создание списка данных (по POST-запросу)
# class WomenAPIList(generics. ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# # Класс обеспечивает изменение конкретной записи
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# # Класс который предоставляет реализацию get(),
# # patch() и delete() по умолчанию.
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer    

