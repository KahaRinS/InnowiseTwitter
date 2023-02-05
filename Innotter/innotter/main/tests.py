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
        user = CustomUser.objects.create_superuser(email='slavakah1@gmail.com', password='slava1234',
                                                   first_name='SLava', last_name='Kulak', username='Admin')
        user.save()
        page = Page.objects.create(name='TestPage', uuid='123456', description='just description for test page', owner=user)
        page.save()

    def test_page_create_from_user_with_page(self):
        acess = self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {acess}'}
        self.client.credentials(**headers)
        response = self.client.post('http://testserver/api/v1/page/',
                                    {'name': 'test2page', 'uuid': '1234', 'description': 'Just some text'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_page_success_create(self):
        user = CustomUser.objects.create_user(email='test@gmail.com', password='slava1234',
                                              first_name='Test', last_name='Test')
        user.save()
        acess = self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'test@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {acess}'}
        self.client.credentials(**headers)
        response = self.client.post('http://testserver/api/v1/page/',
                                    {'name': 'test2page', 'uuid': '1234', 'description': 'Just some text'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_page_create_without_authentication(self):
        response = self.client.post('http://testserver/api/v1/page/',
                                    {'name': 'test2page', 'uuid': '1234', 'description': 'Just some text'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_page_create_with_bad_data(self):
        user = CustomUser.objects.create_user(email='test2@gmail.com', password='slava1234',
                                              first_name='Test', last_name='Test')
        user.save()
        acess = self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'test2@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {acess}'}
        self.client.credentials(**headers)
        response = self.client.post('http://testserver/api/v1/page/',
                                    {'name': 'test3page', 'uuid': '123456', 'description': 'Just some text'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_page_private_list(self):
        user = CustomUser.objects.create_user(email='test@gmail.com', password='slava1234',
                                              first_name='Test', last_name='Test')
        user.save()
        acess = self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'test@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {acess}'}
        self.client.credentials(**headers)
        self.client.post('http://testserver/api/v1/page/',
                                    {'name': 'test2page', 'uuid': '1234', 'description': 'Just some text', 'is_private': 'True'},
                                    format='json')
        response = self.client.get('http://testserver/api/v1/page/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        acess = self.client.post('http://testserver/api/v1/user/login/',
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {acess}'}
        self.client.credentials(**headers)
        response = self.client.post('http://testserver/api/v1/post/',
                                    {'content':'Content for post'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_without_auth(self):
        response = self.client.post('http://testserver/api/v1/post/',
                                    {'content':'Content for post'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)