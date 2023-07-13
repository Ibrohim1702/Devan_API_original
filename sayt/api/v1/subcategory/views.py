from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.v1.subcategory.services import subcategory_format
from api.models import SubCategory
from .serializer import SubcategorySerializer


class SubcategoryView(ListCreateAPIView):
    serializer_class = SubcategorySerializer

    def get(self, requests, pk=None, *args, **kwargs):
        try:
            result = subcategory_format(SubCategory.objects.filter(pk=pk).first())
        except:
            result = "bu pk da sub_category mavjut emas"
        if not pk:
            result = [subcategory_format(i) for i in SubCategory.objects.all()]

        return Response({"data": result})

    def put(self, requests, pk, *args, **kwargs):

        data = requests.data
        new = SubCategory.objects.get(pk=pk)
        serializer = self.get_serializer(data=data, instance=new, partial=True)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        return Response(subcategory_format(root))

    def delete(self, requests, pk, *args, **kwargs):
        prod = SubCategory.objects.filter(pk=pk).first()
        if prod:
            result = "subcategory o'chirildi"
        else:
            result = "subcategory topilmadi"
        return Response({"reultat": result})
