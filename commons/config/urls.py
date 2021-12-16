from django.contrib import admin
from django.urls import include, path

from commons.common.urls import router as common_router

urlpatterns = [
    path('common/', include(common_router.urls)),
]
