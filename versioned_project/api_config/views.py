from rest_framework.views import APIView
from rest_framework.response import Response

# -------- Version 1 View --------
class MessageV1(APIView):
    def get(self, request):
        return Response({
            "version": "v1",
            "message": "Hello from Version 1"
        })


# -------- Version 2 View --------
class MessageV2(APIView):
    def get(self, request):
        return Response({
            "version": "v2",
            "message": "Hello from Version 2",
            "extra_info": "This field exists only in v2"
        })
