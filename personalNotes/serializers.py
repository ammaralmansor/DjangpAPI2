from rest_framework import serializers 
from personalNotes.models import Auther,Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['auther','note']

class AutherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auther
        fields = ['name']

