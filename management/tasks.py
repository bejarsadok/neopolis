from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_task_notification_email(task_id, user_email):
    # Construisez le message d'email
    subject = 'Nouvelle Tâche Assignée'
    message = f'Vous avez été assigné à une nouvelle tâche avec l\'ID {task_id}.'
    from_email = settings.DEFAULT_FROM_EMAIL

    # Envoyez l'email
    send_mail(subject, message, from_email, [user_email])