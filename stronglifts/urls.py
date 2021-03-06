"""stronglifts URL Configuration

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
from django.urls import path, include
from rest_framework import routers

from core.views import (
    CreateUserView,
    ProfileViewSet,
    ExerciseViewSet,
    ExerciseLogViewSet,
    NextExerciseView
)

router = routers.DefaultRouter()

router.register('profile', ProfileViewSet, basename='profile')
router.register('exercises', ExerciseViewSet, basename='exercises')
router.register('exerciselog', ExerciseLogViewSet, basename='exerciselog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/create/', CreateUserView.as_view(), name='create'),
    path('api/v1/', include(router.urls)),
    path('api/v1/next-exercise/', NextExerciseView.as_view(), name='next-exercise'),
    path('auth/', include('djoser.urls.jwt'))
]
