from rest_framework import serializers

from habit.models import HabitTracker


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitTracker
        fields = '__all__'
