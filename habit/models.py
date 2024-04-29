from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class HabitTracker(models.Model):
    name = models.CharField(max_length=50, verbose_name='название привычки')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    time = models.TimeField(default='12:00:00', verbose_name='время', **NULLABLE)
    action = models.CharField(max_length=100, verbose_name='действие', **NULLABLE)
    date = models.DateField(verbose_name='дата', **NULLABLE)
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                      verbose_name='связанная привычка', **NULLABLE)
    reward = models.CharField(max_length=250, verbose_name='вознаграждение', **NULLABLE)
    duration = models.PositiveIntegerField(verbose_name='длительность выполнения', **NULLABLE)
    periodicity = models.IntegerField(default=1, verbose_name='периодичность', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
