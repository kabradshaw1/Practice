from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NoteSerializer
from .models import Notes
from django.shortcuts import render

# Create your views here.
def front(request):
    context = { }
    return render(request, "index.html", context)