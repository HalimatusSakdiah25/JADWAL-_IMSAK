from django.contrib import admin
from django.urls import path, include

from jadwalapp.views import JadwalImsakViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jadwal', JadwalImsakViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
]