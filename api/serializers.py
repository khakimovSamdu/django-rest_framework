from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 200)
    completed = serializers.BooleanField(default = False)
    description = serializers.CharField(default = '')
    created = serializers.DateTimeField(default = datetime.now)

