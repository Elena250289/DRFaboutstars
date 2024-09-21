from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import WomenSerializer
from rest_framework.decorators import action
from .models import Category, Women
from rest_framework.response import Response 


class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet,
                    ):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response ({'cats': [cats.name]})


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

