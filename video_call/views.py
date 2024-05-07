# video_call/views.py
from django.shortcuts import render
from .models import Room

def room_detail(request, room_id):
    room = Room.objects.get(pk=room_id)
    return render(request, 'room_detail.html', {'room': room})
