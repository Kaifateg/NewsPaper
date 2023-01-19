from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import *


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )
    time_create_post = DateTimeFilter(
        field_name='time_create_post',
        lookup_expr='gt',
        label='Create time',
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'name_news': ['icontains'],
        }
