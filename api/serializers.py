from rest_framework import serializers
from .models import Note
class NoteSerializer(serializers.ModelSerializer):
    blog=serializers.StringRelatedField(read_only=True)
    author=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=Note
        fields='__all__'