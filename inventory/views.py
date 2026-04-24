from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stock_items = Product.objects.filter(quantity__lte=models.F('threshold'))
        serializer = self.get_serializer(low_stock_items, many=True)
        return Response(serializer.data)
