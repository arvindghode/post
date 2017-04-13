from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^posts', views.PostViewSet)
router.register(r'^comments', views.CommentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
