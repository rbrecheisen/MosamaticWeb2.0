from django.urls import path

from .views.healthcheck import HealthCheck
from .views.index import Index


urlpatterns = [
    path('', Index.as_view()),
    path('health/', HealthCheck.as_view()),
]
