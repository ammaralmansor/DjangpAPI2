from rest_framework import serializers 
from personalNotes.models import Auther,Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['pk','auther','note']

class AutherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auther
        fields = ['pk','name']

