# Import our Task model
from .models import Task
# Import the serializer we just created
from .serializers import TaskSerializer

# Import django rest framework functions

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create a class based view


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    # Select all tasks
    queryset = Task.objects.all()
    # Serialize data
    serializer_class = TaskSerializer