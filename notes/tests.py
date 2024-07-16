from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Note

User = get_user_model()

class NotesAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.login(username='testuser', password='password')
        self.note = Note.objects.create(title='Test Note', body='This is a test note.', owner=self.user)

        # Obtain token for testuser
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    # def test_signup(self):
    #     url = reverse('signup')
    #     data = {'username': 'newuser', 'password': 'newpassword'}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_login(self):
    #     url = reverse('login')
    #     data = {'username': 'testuser', 'password': 'password'}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_note(self):
        url = reverse('note_list_create')
        data = {'title': 'New Note', 'body': 'This is a new note.'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_notes(self):
        url = reverse('note_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_note_by_id(self):
        url = reverse('note_detail', kwargs={'pk': self.note.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        url = reverse('note_detail', kwargs={'pk': self.note.pk})
        data = {'title': 'Updated Note', 'body': 'This is an updated note.'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note(self):
        url = reverse('note_detail', kwargs={'pk': self.note.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_share_note(self):
        other_user = User.objects.create_user(username='otheruser', password='password')
        url = reverse('share_note', kwargs={'pk': self.note.pk})
        data = {'username': 'otheruser'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
