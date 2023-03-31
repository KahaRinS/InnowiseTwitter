from django_filters import rest_framework as filters
from main.models import Page


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PageFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    tags = CharFilterInFilter(field_name='tags__name', lookup_expr='in')

    class Meta:
        model = Page
        fields = ('name', 'tags')
