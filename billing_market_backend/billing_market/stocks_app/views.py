from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockSerializer, StockSerializer1,Product
from django.shortcuts import get_object_or_404

class StockAPI(APIView):
    

    def get(self, request):
        blogs = Product.objects.all()
        serializer = StockSerializer1(blogs, many=True) # serialize the queryset
        return Response(data= serializer.data)

        

    def post(self, request):
        serializer = StockSerializer(data=request.data) # deserializing the JSON data into python
        if serializer.is_valid():
            obj = serializer.save()
            gst = obj.product_gst.cgst + obj.product_gst.sgst
            print(gst)
            gst_in_rupees = (gst/100) * obj.product_cost_per_quantity
            obj.product_cost_with_gst = obj.product_cost_per_quantity + gst_in_rupees
            print(obj.product_cost_with_gst)
            obj.product_total_cost = obj.product_quantity * obj.product_cost_with_gst
            obj.save() 

            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class  StockDetailAPI(APIView):

    def get(self,request,pk=None):
        obj = get_object_or_404(Product,pk=pk)
        serializer = StockSerializer(obj)
        return Response(data=serializer.data)
    


    def delete(self,request,pk=None):
        obj = get_object_or_404(Product,pk=pk)
        obj.delete()
        return Response(data=None)



    def put(self,request,pk=None):
        obj = get_object_or_404(Product,pk=pk)
        serializer = StockSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def patch(self,request,pk=None):
        obj = get_object_or_404(Product,pk=pk)
        serializer = StockSerializer(data=request.data,instance=obj,partial=True)
        if serializer.is_valid():
            obj = serializer.save()
            gst = obj.product_gst.cgst + obj.product_gst.sgst
            print(gst)
            gst_in_rupees = (gst/100) * obj.product_cost_per_quantity
            obj.product_cost_with_gst = obj.product_cost_per_quantity + gst_in_rupees
            print(obj.product_total_cost_with_gst)
            obj.product_total_cost = obj.product_quantity * obj.product_cost_with_gst
            obj.save()
            serializer = StockSerializer(obj)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)