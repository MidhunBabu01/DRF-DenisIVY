from rest_framework import serializers
from api_app.views import Task





class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'