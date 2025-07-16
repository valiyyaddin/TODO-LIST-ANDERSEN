from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView,UpdateView,DeleteView
from .models import  Task
from django.urls import  reverse_lazy
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    paginate_by = 3


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
class TaskCreate(CreateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskUpdate(UpdateView):

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Hello {request.user.username}'})




def login_page(request):
    return render(request, 'base/login_page.html')



class TaskAPIViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        task = self.get_object()
        if task.user != request.user:
            return Response({'error': 'Not authorized'}, status=403)
        task.status = 'completed'
        task.save()
        return Response({'message': 'Task marked as completed'})