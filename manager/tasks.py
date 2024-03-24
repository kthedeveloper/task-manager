from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_new_task_notification(user_email, task_title):
    subject = "New task!"
    message = f"New task is added to your project: {task_title}"
    send_mail(subject, message, 'from@example.com', [user_email])
