from datetime import datetime
from celery import shared_task
from habit.models import HabitTracker
from habit.services import create_bot_telegram


@shared_task
def send_message_habit():
    now_time = datetime.now().time()
    habits = HabitTracker.objects.all()
    for habit in habits:
        if now_time == habit.time:
            text = f'Я буду {habit.action} в {habit.time} в {habit.place}'
            chat_id = habit.user.chat_id
            create_bot_telegram(chat_id, text)
