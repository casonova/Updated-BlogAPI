from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"comment", CommentView, basename="comment")
urlpatterns = [
    path(
        "",
        include(router.urls),
    ),
    path("post", PostView.as_view(), name="post"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
]
