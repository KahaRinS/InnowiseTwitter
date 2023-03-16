from django.urls import reverse
from main.models import Tag
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import CustomUser
from users.views import *


class MainTests(APITestCase):

    def setUp(self):
        Tag.objects.create(name='Innotter')
        CustomUser.objects.create_superuser(email='slavakah1@gmail.com', username='ADMINUSER', password='slava1234', first_name='SLava', last_name='Kulak')
        self.loginurl = reverse('user-login')
        self.refreshurl = reverse('user-refresh')
        self.registerurl = reverse('user-register')
        self.tagurl = reverse('tag-list')
        self.userurl = reverse('user-list')


    def test_user_authentication(self):
        self.client = APIClient()
        access_token = self.client.post(self.loginurl,
                                      {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        response = self.client.get(self.tagurl)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_fail_authentication(self):
        response = self.client.get(self.tagurl)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_user_registration(self):
        response = self.client.post(self.registerurl,
                                   {'email': 'slavakah2@gmail.com', 'password': 'slava1234', 'username': 'test1user',
                                    'first_name': 'SLava', 'last_name': 'Kulak'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_fail_registration(self):
        response = self.client.post(self.registerurl,
                                   {'first_name': 'SLava', 'last_name': 'Kulak'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_user_login(self):
        response = self.client.post(self.loginurl,
                                   {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_fail_login(self):
        response = self.client.post(self.loginurl,
                                   {'email': 'slavakah@gmail.com', 'password': 'slava123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_user_refresh(self):
        refresh_token = self.client.post(self.loginurl,
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'refresh']
        response = self.client.post(self.refreshurl,
                                    {'refresh_token': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_fail_refresh(self):
        refresh_token = self.client.post(self.loginurl,
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'refresh']
        response = self.client.post(self.refreshurl,
                                    {'refresh_token': refresh_token+'d'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_filter(self):
        access_token = self.client.post(self.loginurl,
                                        {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        CustomUser.objects.create_superuser(email='slavakah2@gmail.com', password='slava1234',
                                                   first_name='SLava', last_name='Kulak', username='Abudabi')
        url = f'{self.userurl}?username=Abu'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)