from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        read_only_fields = ['id']

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'priority', 'owner']
        read_only_fields = ['id']