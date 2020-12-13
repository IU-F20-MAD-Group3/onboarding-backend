from django.contrib import admin
from django.urls import path

from rest_framework import routers
from rest_framework.authtoken import views

from .views import ChecklistViewSet

router = routers.SimpleRouter()
router.register('checklists', ChecklistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tokens/', views.obtain_auth_token),
]

urlpatterns += router.urls
