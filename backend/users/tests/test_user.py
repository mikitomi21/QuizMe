from django.test import TestCase
from django.db import transaction
from django.contrib.auth.hashers import check_password
from users.factories import UserFactory
from users.models import CustomUser


class TestUser(TestCase):
    def setUp(self):
        self.username = "test"
        self.email = "test@test.com"
        self.password = "zaq1@WSX"

    def tearDown(self):
        CustomUser.objects.filter(email=self.email).delete()

    def test_create_user(self):
        user = CustomUser.objects.create(username=self.username, email=self.email)

        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)

    def test_set_password(self):
        user = CustomUser.objects.create(username=self.username, email=self.email)

        user.set_password(self.password)
        self.assertTrue(check_password(self.password, user.password))

    def test_create_two_users_with_the_same_emails(self):
        with transaction.atomic():
            with self.assertRaises(Exception):
                for i in range(2):
                    CustomUser.objects.create(username=f"{self.username}{i}", email=self.email)

    def test_create_two_users_with_the_same_usernames(self):
        with transaction.atomic():
            with self.assertRaises(Exception):
                for i in range(2):
                    CustomUser.objects.create(username=self.username, email=f"{self.email}{i}")
