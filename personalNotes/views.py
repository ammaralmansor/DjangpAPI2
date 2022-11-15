from django.shortcuts import render
from .models import Auther,Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AutherSerializer , NoteSerializer
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK
# Create your views here.


#Adding a note.
#Listing all notes.
@api_view(['GET','POST'])
def Listing_Adding_Note(request):
    if request.method == 'GET':
        notes = Note.objects.all() 
        serializer = NoteSerializer(notes , many = True) 
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == 'POST':
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.data,status=HTTP_400_BAD_REQUEST)


#Adding a Auther.
#Listing all Authers.
@api_view(['GET','POST'])
def Listing_Adding_Auther(request):
    if request.method == 'GET':
        authers = Auther.objects.all() 
        serializer = AutherSerializer(authers , many = True) 
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AutherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.data,status=HTTP_400_BAD_REQUEST)



#Deleting a note.
#Retrieving one note by id.
@api_view(['GET','PUT','DELETE'])
def Deleting_Retrieving_Putting_one_note (request , pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    #GET
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.error,status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=HTTP_200_OK)