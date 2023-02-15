from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
        lookup_expr='gt',
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['icontains'],

        }
