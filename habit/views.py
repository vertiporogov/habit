from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import HabitTracker
from habit.pagination import HabitPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        queryset = HabitTracker.objects.filter(owner=user)
        return queryset


class HabitRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для вывода привычки
    """
    serializer_class = HabitSerializer
    queryset = HabitTracker.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    """
    Контроллер для изменения привычки
    """
    serializer_class = HabitSerializer
    queryset = HabitTracker.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """
    Контроллер для удаления привычки
    """
    queryset = HabitTracker.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListAPIView(ListAPIView):
    """
    Контроллер для вывода списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = HabitTracker.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination
