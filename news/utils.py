from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPaper import settings


def send_notifications(preview, pk, title, followers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=followers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()