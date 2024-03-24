from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Project, Task, Comment
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(viewsets.ModelViewSet):
    """ A viewset for viewing and editing project instances"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated & IsManager]


class TaskViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing task instances"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        """
        Optionally restricts the returned tasks to a given project,
        by filtering against a 'project' query parameter in the URL
        """
        queryset = Task.objects.all()
        project_id = self.request.query_params.get('project')
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewind and editing comment instances
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = IsAuthenticated

    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given project,
        by filtering against a 'task' query parameter in the URL

        """
        queryset = Comment.objects.all()
        task_id = self.request.query_params.get('task')
        if task_id is not None:
            queryset = queryset.filter(task_id=task_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
