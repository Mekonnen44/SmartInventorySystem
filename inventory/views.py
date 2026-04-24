from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stock_items = Product.objects.filter(quantity__lte=models.F('threshold'))
        serializer = self.get_serializer(low_stock_items, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def total_stock(self, request):
        total_stock = Product.objects.aggregate(Sum('quantity'))
        return Response({'total_stock': total_stock['quantity__sum']})

    @action(detail=False, methods=['get'])
    def sales_trends(self, request):
        mock_sales_trends = {
            'weekly': ["low", "medium", "high"],
            'monthly': ["medium", "high", "medium"],
        }
        return Response(mock_sales_trends)
