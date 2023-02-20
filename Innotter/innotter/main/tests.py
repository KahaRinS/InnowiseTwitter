from django.test import TestCase
from django.urls import reverse
from main.models import Page, Post, Tag
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class MainTests(APITestCase):

    def setUp(self):
        Tag.objects.create(name='Innotter')
        user = CustomUser.objects.create_superuser(email='slavakah1@gmail.com', password='slava1234',
                                                   first_name='SLava', last_name='Kulak', username='Admin')
        Page.objects.create(name='TestPage', description='just description for test page', owner=user)
        self.loginurl = reverse('user-login')
        self.pageurl = reverse('page-list')
        self.posturl = reverse('post-list')

    def test_page_create_from_user_with_page(self):
        access_token = self.client.post(self.loginurl,
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        response = self.client.post(self.pageurl,
                                    {'name': 'test2page', 'description': 'Just some text'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_page_success_create(self):
        CustomUser.objects.create_user(email='test@gmail.com', password='slava1234',
                                              first_name='Test', last_name='Test')
        access_token = self.client.post(self.loginurl,
                                 {'email': 'test@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        response = self.client.post(self.pageurl,
                                    {'name': 'test2page', 'description': 'Just some text'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_page_create_without_authentication(self):
        response = self.client.post(self.pageurl,
                                    {'name': 'test2page', 'description': 'Just some text'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_page_create_with_bad_data(self):
        CustomUser.objects.create_user(email='test2@gmail.com', password='slava1234',
                                              first_name='Test', last_name='Test')
        access_token = self.client.post(self.loginurl,
                                 {'email': 'test2@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        response = self.client.post(self.pageurl,
                                    {'name': 'TestPage', 'description': 'Just some text'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_page_private_list(self):
        CustomUser.objects.create_user(email='test@gmail.com', password='slava1234',
                                              first_name='Test', last_name='Test')
        access_token = self.client.post(self.loginurl,
                                 {'email': 'test@gmail.com', 'password': 'slava1234'}, format='json').data[
            'access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        self.client.post(self.pageurl,
                                    {'name': 'test2page', 'description': 'Just some text', 'is_private': 'True'},
                                    format='json')
        response = self.client.get(self.pageurl)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        access_token = self.client.post(self.loginurl,
                                 {'email': 'slavakah1@gmail.com', 'password': 'slava1234'}, format='json').data['access']
        headers = {'Authorization': f'Token {access_token}'}
        self.client.credentials(**headers)
        response = self.client.post(self.posturl,
                                    {'content':'Content for post'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_without_auth(self):
        response = self.client.post(self.posturl,
                                    {'content':'Content for post'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)