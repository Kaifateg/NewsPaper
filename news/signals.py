from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from news.models import PostCategory
from news.utils import send_notifications


@receiver(m2m_changed, sender=PostCategory)
def new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        followers_emails = []

        for category in categories:
            followers = category.follower.all()
            followers_emails += [f.email for f in followers]

        send_notifications(instance.preview(), instance.pk, instance.name_news, followers_emails)