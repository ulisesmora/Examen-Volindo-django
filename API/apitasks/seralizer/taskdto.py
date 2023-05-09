from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class taskSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

    def validate(self, validated_data):
        title=validated_data['title'],
        description=validated_data['description'],
        return validated_data