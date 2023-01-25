from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import datetime

from NewsPaper import settings
from news.models import Post, Category


@shared_task
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

@shared_task
def posts_of_the_week():
    today = datetime.datetime.now()
    last_weak = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_create_post__gt=last_weak)
    categories = set(posts.values_list('category__name_category', flat=True))
    followers = set(Category.objects.filter(name__in=categories).values_list('followers__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Posts of the weak',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=followers,
    )

    msg.attach_alternative(html_content, 'text/html')