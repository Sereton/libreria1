from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'pamchito', email='pam@chito.com',password='1234bzrp'
        )
        self.assertEqual(user.username,"pamchito")
        self.assertEqual(user.email, "pam@chito.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = 'pamchito', email='pam@chito.com',password='1234bzrp'
        )
        self.assertEqual(user.username,"pamchito")
        self.assertEqual(user.email, "pam@chito.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)



