from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskAPIViewSet, HelloView, login_page, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'api/tasks', TaskAPIViewSet, basename='tasks')

urlpatterns = [
    # Default home page -> login
    path('', login_page, name='login'),

    # Web views
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),

    # JWT and API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('login/', login_page, name='login'),
]
