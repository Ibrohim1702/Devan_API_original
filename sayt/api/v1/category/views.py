from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.v1.category.services import category_format
from api.models import Category
from .serializer import CategorySerializer


class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get(self, requests, pk=None, *args, **kwargs):
        try:
            result = category_format(Category.objects.filter(pk=pk).first())
        except:
            result = "bu pk da category mavjut emas"
        if not pk:
            result = [category_format(i) for i in Category.objects.all()]

        return Response({"data": result})

    def put(self, requests, pk, *args, **kwargs):

        data = requests.data
        new = Category.objects.get(pk=pk)
        serializer = self.get_serializer(data=data, instance=new, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response(category_format(root))

    def delete(self, requests, pk, *args, **kwargs):
        prod = Category.objects.filter(pk=pk).first()
        if prod:
            # prod.delete()
            result = "category o'chirildi"
        else:
            result = "category topilmadi"
        return Response({"reultat": result})
