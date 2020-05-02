from django.core.mail import send_mail
import django_rq

from smartedu.settings import ADMIN_EMAILS, EMAIL_HOST_USER

queue = django_rq.get_queue("email")


def send_contact_us_email_to_admins(subject, body, email):
    try:
        send_mail(
            subject=f'You have new message "{subject}"',
            message=f'You have message \n\n"{body}"\n\n from {email}',
            recipient_list=ADMIN_EMAILS,
            from_email=EMAIL_HOST_USER,
        )
    except Exception as ex:
        print("send_contact_us_email_to_admins.ex", ex)
        raise ex


def send_contact_us_email_to_user(subject, body, email):
    try:
        send_mail(
            subject=f'Thanks for you message "{subject}"',
            message=f'Your message \n\n"{body}"\n\n is sent to admins',
            recipient_list=[email],
            from_email=EMAIL_HOST_USER,
        )
    except Exception as ex:
        print("send_contact_us_email_to_user.ex", ex)
        raise ex


def send_contact_us_email(subject, body, email):
    queue.enqueue(send_contact_us_email_to_user, subject, body, email)
    queue.enqueue(send_contact_us_email_to_admins, subject, body, email)
