# video_call/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Room

class RoomDetailViewTest(TestCase):
    def test_room_detail_view(self):
        room = Room.objects.create(name="Test Room")
        response = self.client.get(reverse('room_detail', args=[room.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, room.name)
