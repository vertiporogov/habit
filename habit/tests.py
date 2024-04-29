from rest_framework.test import APITestCase
from django.contrib.auth.models import Group

from django.urls import reverse
from rest_framework import status

from habit.models import HabitTracker
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test1@test1.com', is_superuser=True
        )

        self.habit = HabitTracker.objects.create(
            name='Test',
            place='Test',
            action='Test'
        )

        moderator_group, created = Group.objects.get_or_create(name='moders')

        self.user = User.objects.create(email='test@test.com', is_superuser=True)
        self.user.groups.add(moderator_group)

    def test_get_list(self):
        """ Тест для получения списка привычек """

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('habit:habit-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_habit(self):
        """ Тест создания привычек """

        self.client.force_authenticate(user=self.user)

        data = {
            "name": self.habit.name,
            "place": self.habit.place,
            "owner": self.user.id,
            "action": self.habit.action
        }

        response = self.client.post(
            reverse('habit:habit-create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            HabitTracker.objects.all().exists()
        )

        self.assertEqual(
            response.json()['name'],
            data['name']
        )

        self.assertEqual(
            response.json()['place'],
            data['place']
        )

        self.assertEqual(
            response.json()['action'],
            data['action']
        )

    def test_update_habit(self):
        """Тестирование изменения информации о привычке"""
        self.client.force_authenticate(user=self.user)
        habit = HabitTracker.objects.create(
            name='Test_habit',
            place='Test_habit',
            action='Test_habit',
            owner=self.user
        )

        response = self.client.patch(
            f'/update/{habit.id}/',
            {'place': 'Test_habit',
             'action': 'Test_habit',
             'owner': self.user.id, }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        self.client.force_authenticate(user=self.user)

        habit = HabitTracker.objects.create(
            name='Test_habit',
            place='Test_habit',
            action='Test_habit',
            owner=self.user
        )

        response = self.client.delete(
            f'/delete/{habit.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_duration_habit(self):
        """Тестирование создания привычки со временем исполнения более 2 минут"""

        self.client.force_authenticate(user=self.user)

        data = {
            "name": self.habit.name,
            "place": self.habit.place,
            "owner": self.user.id,
            "action": self.habit.action,
            "duration": 130
        }

        response = self.client.post(
            reverse('habit:habit-create'),
            data=data
        )

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Выполнение привычки не может превышать 120 секунд']}
        )

    def test_periodicity_habit(self):

        """Тестирование периодичности привычки"""

        self.client.force_authenticate(user=self.user)

        data = {
            "name": self.habit.name,
            "place": self.habit.place,
            "owner": self.user.id,
            "action": self.habit.action,
            "periodicity": 8
        }

        response = self.client.post(
            reverse('habit:habit-create'),
            data=data
        )

        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {'non_field_errors': ['Периодичность привычки не может быть больше 7 и меньше 1']}
        )
