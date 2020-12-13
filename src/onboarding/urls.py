from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views

from .views import ChecklistViewSet

router = routers.SimpleRouter()
router.register('checklists', ChecklistViewSet)

api_urlpatterns = [
    path('tokens/', views.obtain_auth_token),
] + router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]
