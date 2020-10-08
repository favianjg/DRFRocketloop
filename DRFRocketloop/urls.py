"""DRFRocketloop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from boards.views import BoardViewSet, TodoViewSet, TodoNotDoneViewSet, BoardDetailViewSet
from reminder.views import ReminderViewSet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reminders', ReminderViewSet)
router.register(r'board_overview', BoardViewSet)
router.register(r'board_detail', BoardDetailViewSet)
router.register(r'todo_list', TodoViewSet)
router.register(r'todo_notdone', TodoNotDoneViewSet, basename='Todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('boards.urls')),
    path('', include('reminder.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
