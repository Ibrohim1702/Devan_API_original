from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.v1.product.services import product_format
from api.models import Product
from .serializer import ProductSerializer


class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer

    def get(self, requests, pk=None, *args, **kwargs):
        try:
            result = product_format(Product.objects.filter(pk=pk).first())
        except:
            result = "bu pk da product mavjut emas"
        if not pk:
            result = [product_format(i) for i in Product.objects.all()]

        return Response({"data": result})

    def put(self, requests, pk, *args, **kwargs):

        data = requests.data
        new = Product.objects.get(pk=pk)
        serializer = self.get_serializer(data=data, instance=new, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response(product_format(root))

    def delete(self, requests, pk, *args, **kwargs):
        prod = Product.objects.filter(pk=pk).first()
        if prod:
            result = "product o'chirildi"
        else:
            result = "product topilmadi"
        return Response({"reultat": result})
