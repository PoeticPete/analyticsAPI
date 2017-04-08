from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, SystemOverview, SystemState


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'

class SystemSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemOverview
        fields = '__all__'

class SystemStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemState
        fields = '__all__'