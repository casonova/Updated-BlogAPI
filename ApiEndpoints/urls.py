from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"comment", CommentView, basename="comment")
urlpatterns = [
    path("", include(router.urls),),
    path("post", PostView.as_view(), name="post"),
    path("post/<int:pk>/", PostView.as_view(), name="post"),
    # path("comment", CommentApiView.as_view(), name="comment"),
    # path("comment/<int:pk>", CommentApiView.as_view(), name="comment"),
]
    