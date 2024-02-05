from django.contrib.auth.models import User
from django.test import TestCase

from ApiEndpoints.models import Comment, Post


class PostModelTestCse(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            email="zainab@gmail.com",
            username="zainab",
            first_name="zainab",
            last_name="jabar",
            password="zainab",
        )
        self.post = Post.objects.create(
            title="Sicology",
            post_body="Every body should learn sociology",
            user_type=self.user1,
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Sicology")


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            email="zainab@gmail.com",
            username="zainab",
            first_name="zainab",
            last_name="jabar",
            password="zainab",
        )
        self.post = Post.objects.create(
            title="Sicology",
            post_body="Every body should learn sociology",
            user_type=self.user1,
        )
        self.comment = Comment.objects.create(
            post=self.post, user_type=self.user1, comment_body="body"
        )

    def test_post_creation(self):
        self.assertEqual(self.comment.post.title, "Sicology")
        self.assertEqual(self.comment.comment_body, "body")
