import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Введите слово для поиска"
    )
    date = django_filters.DateFromToRangeFilter(
        label="Дата от и до",
        field_name="date",
        widget=django_filters.widgets.RangeWidget(attrs={"type": "date"})
    )

    class Meta:
        model = Message
        fields = [
            "chat"
        ]