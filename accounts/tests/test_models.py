import uuid as uuid_lib
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()


class UserModelTests(TestCase):

    def test_create_user_with_email(self):
        user = User.objects.create_user(
            email="user@example.com",
            password="strong-password",
        )

        self.assertEqual(user.email, "user@example.com")
        self.assertTrue(user.check_password("strong-password"))

    def test_username_is_set_from_email_on_create(self):
        user = User.objects.create_user(
            email="user@example.com",
            password="password",
        )

        self.assertEqual(user.username, "user@example.com")
    
    def test_username_updates_when_email_changes(self):
        user = User.objects.create_user(
            email="old@example.com",
            password="password",
        )

        user.email = "new@example.com"
        user.save()

        user.refresh_from_db()
        self.assertEqual(user.username, "new@example.com")
    
    def test_uuid_is_created(self):
        user = User.objects.create_user(
            email="user@example.com",
            password="password",
        )

        self.assertIsNotNone(user.uuid)
        self.assertIsInstance(user.uuid, uuid_lib.UUID)

    def test_email_is_unique(self):
        User.objects.create_user(
            email="unique@example.com",
            password="password",
        )

        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="unique@example.com",
                password="password",
            )



