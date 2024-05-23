from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views import CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("tasks", TaskViewSet)

api_v1_urls = (router.urls, "v1")

urlpatterns = [path("v1/", include(api_v1_urls))]
