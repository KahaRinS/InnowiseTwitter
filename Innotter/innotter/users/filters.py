from django_filters import rest_framework as filters
from users.models import CustomUser


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(field_name='username',
                                  lookup_expr='icontains')

    class Meta:
        model = CustomUser
        fields = ('username',)
