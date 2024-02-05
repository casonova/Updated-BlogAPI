from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ApiEndpoints.models import Comment, Post
from ApiEndpoints.views import *


class TestView(APITestCase):
    factory = APIRequestFactory()

    # Urls of Views
    post_url = reverse("post")
    token = reverse("token_obtain_pair")

    # url = reverse("blog-detail")
    def setUp(self):
        self.user1 = User.objects.create(
            email="zainab@gmail.com",
            username="zainab",
            first_name="zainab",
            last_name="jabbar",
            password="zainab",
        )

        self.user2 = User.objects.create(
            email="zubair@gmail.com",
            username="zubair",
            first_name="zubair",
            last_name="ahmed",
            password="zubair",
            is_superuser=True,
            is_staff=True,
        )

        self.post = Post.objects.create(
            title="Sicology", post_body="Sicology", user_type=self.user1
        )
        self.comment = Comment.objects.create(
            post=self.post, user_type=self.user2, comment_body="body"
        )

        self.user_data = {
            "email": "ali@gmail.com",
            "username": "ali",
            "first_name": "ali",
            "last_name": "ahmed",
            "password": "ali",
        }

        self.post_data = {
            "title": "Terminology",
            "post_body": "sicology",
            "user_type": 1,
        }

        self.comment_data = {"post": 1, "comment_body": "sicology", "user_type": 1}

        self.client = APIClient()
        data = {"username": "zubair", "password": "zubair"}
        response = self.client.post(
            "http://127.0.0.1:8000/api/token/",
            {"username": self.user2.username, "password": self.user2.password},
            format="json",
        )
        # print(response)
        self.token1 = response.data.get("access")
        # print(self.token1)
        self.refresh_token = response.data.get("refresh")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token1}")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    # =========== GET Request API Test ============================#

    def test_get_post_with_authenticated(self):
        client = APIClient()
        client.force_authenticate(user=self.user2)
        responce = client.get(self.post_url)
        self.assertEqual(responce.status_code, 200)

    def test_get_post_with_unauthenticated(self):
        client = APIClient()
        responce = client.get(self.post_url)
        self.assertEqual(responce.status_code, 401)

    def test_get_comment(self):
        url = reverse("comment-list")
        client = APIClient()
        client.force_authenticate(user=self.user1)
        responce = client.get(url)
        self.assertEqual(responce.status_code, 200)

    # =========== POST Request API Test ============================#

    def test_create_post(self):
        client = APIClient()
        client.force_authenticate(user=self.user2)
        responce = client.post(self.post_url, self.post_data, format="json")
        self.assertEqual(responce.status_code, 201)

    def test_create_post_unauthenticated(self):
        client = APIClient()
        responce = client.post(self.post_url, self.post_data, format="json")
        self.assertEqual(responce.status_code, 401)

    def test_create_comment(self):
        url = reverse("comment-list")
        client = APIClient()
        client.force_authenticate(user=self.user1)
        response = client.post(url, data=self.comment_data, format="json")
        self.assertEqual(response.status_code, 201)

    # #================= Update Request API Test ==================#

    def test_update_post_data_put_authenticated(self):
        data = {"title": "Narnia", "post_body": "Sicology", "user_type": 1}
        client = APIClient()
        client.force_authenticate(user=self.user2)
        url = reverse("post", kwargs={"pk": self.post.id})
        responce = client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 200)

    def test_update_post_data_put_unauthenticated(self):
        client = APIClient()
        data = {"title": "Narnia", "post_body": "Sicology", "user_type": 1}
        url = reverse("post", kwargs={"pk": self.post.id})
        responce = client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 401)

    def test_update_post_data_patch_unauthenticated(self):
        client = APIClient()
        data = {
            "blog": 1,
            "title": "Narnia Lullabay",
            "body": "Sicology",
            "user_type": 1,
        }
        url = reverse("post", kwargs={"pk": self.post.id})
        responce = client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 401)

    def test_update_comment_data_put_authenticated(self):
        data = {"post": 1, "comment_body": "Youtube", "user_type": 2}
        client = APIClient()
        client.force_authenticate(user=self.user1)
        url = reverse("comment-detail", kwargs={"pk": self.comment.id})
        responce = client.put(url, data, format="json")
        self.assertEqual(responce.status_code, 200)

    def test_update_comment_data_patch_authenticated(self):
        data = {"post": 1, "comment_body": "Billa", "user_type": 2}
        client = APIClient()
        client.force_authenticate(user=self.user1)
        url = reverse("comment-detail", kwargs={"pk": self.comment.id})
        responce = client.put(url, data, format="json")
        # import pdb; pdb.set_trace()
        self.assertEqual(responce.status_code, 200)

    # #================= Delete Request API Test ==================#

    def test_delete_post(self):
        client = APIClient()
        client.force_authenticate(user=self.user2)
        url = reverse("post", kwargs={"pk": self.post.id})
        responce = client.delete(url)
        self.assertEqual(responce.status_code, 200)

    def test_delete_comment(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        url = reverse("comment-detail", kwargs={"pk": self.comment.id})
        responce = client.delete(url)
        self.assertEqual(responce.status_code, 204)
