from celery import app
from django.core.mail import send_mail
from django.conf import settings
from Tasker.celery import app


@app.task
def send_task_assigned_email(user_email, task_title):
    send_mail(
        subject='New task!',
        message=f'You have been assigned to a new task: {task_title}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
    )

