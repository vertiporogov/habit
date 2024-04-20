from rest_framework import serializers

from habit.models import HabitTracker
from habit.validators import (RelateRewardValidator, HabitRelatedHabitIsPleasantValidator, HabitPleasantValidator,
                                CheckInterval, CheckTime)


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Habit """
    class Meta:
        model = HabitTracker
        fields = '__all__'
        validators = [
            RelateRewardValidator(field1='related_habit', field2='reward'),
            HabitRelatedHabitIsPleasantValidator(field1='related_habit', field2='is_pleasant'),
            HabitPleasantValidator(field1='related_habit', field2='reward', field3='is_pleasant'),
            CheckTime(field='duration'),
            CheckInterval(field='periodicity')
        ]
