from django.test import TestCase
from django.urls import reverse
from main.models import Page, Post, Tag
from rest_framework import status
from rest_framework.test import (APIClient, APITestCase, CoreAPIClient,
                                 RequestsClient)
from users.models import CustomUser

# Create your tests here.

class MainTests(APITestCase):

    def setUp(self):
        tag = Tag.objects.create(name='Innotter')
        tag.save()
        user = CustomUser.objects.create_superuser(email='slavakah1@gmail.com', password='slava1234', first_name='SLava', last_name='Kulak')
        user.save()


    def test_user_authentication(self):
        self.client = APIClient()
        acess = self.client.post('http://testserver/api/v1/user/login/',
                                      {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {acess}'}
        self.client.credentials(**headers)
        response = self.client.get('http://testserver/api/v1/tag/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_fail_authentication(self):
        response = self.client.get('http://testserver/api/v1/tag/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_user_registration(self):
        response = self.client.post('http://testserver/api/v1/user/register/',
                                   {'email': 'slavakah2@gmail.com', 'password': 'slava1234', 'username': 'test1user',
                                    'first_name': 'SLava', 'last_name': 'Kulak'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_fail_registration(self):
        response = self.client.post('http://testserver/api/v1/user/register/',
                                   {'email': 'slavakah3@gmail.com', 'username': 'test_fail_user',
                                    'first_name': 'SLava', 'last_name': 'Kulak'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_user_login(self):
        response = self.client.post('http://testserver/api/v1/user/login/',
                                   {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_fail_login(self):
        response = self.client.post('http://testserver/api/v1/user/login/',
                                   {'email': 'slavakah@gmail.com', 'password': 'slava123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_user_refresh(self):
        refresh= self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'refresh']
        response = self.client.post('http://testserver/api/v1/user/refresh/',
                                    {'refresh_token': refresh}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_fail_refresh(self):
        refresh= self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'refresh']
        response = self.client.post('http://testserver/api/v1/user/refresh/',
                                    {'refresh_token': refresh+'d'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)