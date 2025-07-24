from django.urls import path, include
from rest_framework import routers
from apiapp.views import PatientViewSet



router = routers.DefaultRouter()
router.register('patient', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

