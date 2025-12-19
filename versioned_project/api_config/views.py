from rest_framework.views import APIView
from rest_framework.response import Response

# -------- Version 1 View --------
class MessageV1(APIView):
    def get(self, request):
        return Response({
            "version": "v1",
            "message": "Hello from Version 1"
        })

class MessageH1(APIView):
    def get(self, request):
        return Response({
            "version": "v1",
            "message": "Hello from Version 1"
        })
    
class MessageH3(APIView):
    def get(self, request):
        return Response({
            "version": "v1",
            "message": "Hello from Version 1"
        })

class MessageH4(APIView):
    def get(self, request):
        return Response({
            "version": "v1",
            "message": "Hello from Version 1"
        })

class MessageH5(APIView):
    def get(self, request):
        return Response({
            "version": "v1",
            "message": "Hello from Version 1"
        })
