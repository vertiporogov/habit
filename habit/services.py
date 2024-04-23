from django_celery_beat.models import IntervalSchedule, PeriodicTask
import json
from datetime import datetime, timedelta
from config import settings
import requests


def create_interval(habit):
    """ Создаем периодическую задачу """

    schedule, created = IntervalSchedule.objects.get_or_create(
        every=habit.periodicity,
        period=IntervalSchedule.DAYS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name='Habit',
        task='habit.tasks.send_message_habit',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )


def create_bot_telegram(chat_id, text):

    url = 'https://api.telegram.org/bot'
    token = settings.TOKEN_TELEGRAM

    requests.post(
        url=f'{url}{token}/sendMessage',
        data={
            'chat_id': chat_id,
            'text': text
        }
    )
    print(f'chat_id={chat_id}, text={text}')
    print('Отправлен запрос на отправку сообщения')
