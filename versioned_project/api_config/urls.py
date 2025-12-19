from django.urls import path
from .views import MessageV1, MessageV2

urlpatterns = [
    path('v1/message/', MessageV1.as_view()),
    path('v2/message/', MessageV2.as_view()),
]
