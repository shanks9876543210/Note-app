from django.shortcuts import render
from rest_framework import mixins,generics
from .models import Note
from rest_framework import status
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class NoteListCreateCon(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-updated')
    serializer_class = NoteSerializer

class NoteView(APIView):

    def get(self, request, pk):
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk):
       note = Note.objects.get(pk=pk)
       serializer = NoteSerializer(note, data=request.data)

       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           #


    def delete (self, request, pk):
       note = Note.objects.get(pk=pk)
       note.delete()
       return Response('Deleted')
