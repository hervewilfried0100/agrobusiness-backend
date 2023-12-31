from django_filters import rest_framework as filters

from advert.models import OrderStatus


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    min_quantity = filters.NumberFilter(field_name="quantity", lookup_expr="gte")
    max_quantity = filters.NumberFilter(field_name="quantity", lookup_expr="lte")
    category = filters.CharFilter(field_name="category__slug", lookup_expr="iexact")
    stock_status = filters.CharFilter(field_name="stock_status", lookup_expr="iexact")
    store = filters.CharFilter(field_name="store__id", lookup_expr="iexact")
    made_in = filters.CharFilter(field_name="made_in__id", lookup_expr="iexact")


class SellerDeliveryFilter(filters.FilterSet):
    store = filters.CharFilter(field_name="store__id", lookup_expr="iexact")


class OrderFilter(filters.FilterSet):
    reference = filters.CharFilter(lookup_expr="icontains")
    status = filters.CharFilter(lookup_expr="iexact")
    state = filters.CharFilter(method="filter_by_status")
    user = filters.CharFilter(field_name="user__id", lookup_expr="iexact")
    store = filters.CharFilter(field_name="store__id", lookup_expr="iexact")
    min_total_price = filters.NumberFilter(field_name="total_price", lookup_expr="gte")
    max_total_price = filters.NumberFilter(field_name="total_price", lookup_expr="lte")
    

    def filter_by_status(self, queryset, name, value):
        if value.lower() == "active":
            return queryset.exclude(status__in=[OrderStatus.CANCELED.value, OrderStatus.DELIVERED.value])
        elif value.lower() == "inactive":
            return queryset.filter(status__in=[OrderStatus.CANCELED.value, OrderStatus.DELIVERED.value])
        return queryset