from rest_framework.views import APIView
from .models import Order
from .serializers import OrderModelSerializer
import logging
from rest_framework.response import Response

logby = logging.getLogger("gujar")


class OrderAPI(APIView):

    def get(self, request):
        obj = Order.objects.all()
        if len(obj)<=0:
            logby.error("No Record Found")
        else:
            logby.info("Record found") 
        form = OrderModelSerializer(obj, many=True)
        return Response(data=form.data)
    
    def post(self, request):
        form = OrderModelSerializer(data=request.data)
        if form.is_valid():
            form.save()
            logby.info("New Record Created")
            return Response(data=form.data)
        return Response(data=form.errors)
    
class OrderDetailsAPI(APIView):
    def get(self, request, pk=None):
        try:
            obj = Order.objects.get(pk=pk)
            logby.info("Record Found")
        except:
            logby.error("No record Found")
            return Response(data={"message":"Details Not Found"})                 
        form = OrderModelSerializer(instance=obj)
        return Response(data=form.data)
    
    def put(self, request, pk=None):
        try:
            obj = Order.objects.get(pk=pk)
            logby.info("Record Found")
        except:
            logby.error("No record Found")
            return Response(data={"message":"Details Not Found"})
        form = OrderModelSerializer(instance=obj, data=request.data)
        if form.is_valid():
            form.save()
            logby.info("Record Fully updated ok")
            return Response(data=form.data)
        return Response(data=form.errors)
    
    def patch(self, request, pk=None):
        try:
            obj = Order.objects.get(pk=pk)
            logby.info("Record Found")
        except:
            logby.error("No record Found")
            return Response(data={"message":"Details Not Found"})
        form = OrderModelSerializer(instance=obj, data=request.data, partial=True)
        if form.is_valid():
            form.save()
            logby.info("Record partial update successfully")
            return Response(data=form.data)
        return Response(data=form.errors)

    def delete(self, request, pk=None):
        try:
            obj = Order.objects.get(pk=pk)
            logby.info("Record Found")
        except:
            logby.error("No record Found")
            return Response(data={"message":"Details Not Found"})
        obj.delete()
        logby.info("Record Delete Successfully")
        return Response(data={"message": "Record delete sccessfully"})
        

print("hello")