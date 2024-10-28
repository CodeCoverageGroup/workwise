from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationTests(APITestCase):
    def test_user_registration(self):
        url = reverse('user_register')
        data = {
            "username": "newuser",
            "password": "newpassword123",
            "email": "newuser@example.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_registration_with_existing_username(self):
        User.objects.create_user(username="existinguser", password="password123")
        url = reverse('user_register')
        data = {
            "username": "existinguser",
            "password": "anotherpassword123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Username already exists")


class UserLoginAndTokenTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
    
    def test_token_obtain_pair(self):
        url = reverse('token_obtain_pair')
        data = {
            "username": "testuser",
            "password": "password123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        url = reverse('token_refresh')
        data = {"refresh": str(refresh)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


class ProtectedViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="protecteduser", password="password123")
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_access_protected_view(self):
        url = reverse('protected_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "This is a protected view.")

    def test_access_protected_view_without_auth(self):
        self.client.credentials()  # Remove any authentication
        url = reverse('protected_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserCRUDTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username="adminuser", password="adminpass123")
        self.client.force_authenticate(user=self.admin_user)
        self.user = User.objects.create_user(username="regularuser", password="password123")

    def test_user_list(self):
        url = reverse('user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_user_detail_retrieve(self):
        url = reverse('user_detail', args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], "regularuser")

    def test_user_update(self):
        url = reverse('user_detail', args=[self.user.pk])
        data = {"first_name": "UpdatedName"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "UpdatedName")

    def test_user_delete(self):
        url = reverse('user_detail', args=[self.user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
