from django_filters import filters

import core.models


class BookFilter(filters.Filter):
    name = filters.Filter()

    class Meta:
        model = core.models.Book
        fields = ('name')