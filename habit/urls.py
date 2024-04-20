from habit.apps import HabitConfig
from habit.views import HabitListAPIView, HabitCreateAPIView
from django.urls import path

app_name = HabitConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='list'),
    path('create/', HabitCreateAPIView.as_view(), name='create')
    ]