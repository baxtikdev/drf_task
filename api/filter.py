from django.db.models import Q
from rest_framework.filters import BaseFilterBackend


class LocationFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        q = request.query_params.get('q')
        if q:
            query = q.split()
            query_objects = Q()
            for part in query:
                query_objects &= Q(name__icontains=part)
            queryset = queryset.filter(query_objects)

        return queryset


class OfficeFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filters = {}
        fields = ['location']

        for field in fields:
            param_value = request.query_params.get(field, None)
            if param_value is not None:
                filters[f'{field}__exact'] = param_value

        q = request.query_params.get('q')
        if q:
            query = q.split()
            query_objects = Q()
            for part in query:
                query_objects &= Q(name__icontains=part)
            queryset = queryset.filter(query_objects)

        return queryset


class RoomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filters = {}
        fields = ['office']

        for field in fields:
            param_value = request.query_params.get(field, None)
            if param_value is not None:
                filters[f'{field}__exact'] = param_value

        min = request.query_params.get('min')
        max = request.query_params.get('max')
        if min:
            filters[f'capacity__gte'] = min
        if max:
            filters[f'capacity__lte'] = max

        q = request.query_params.get('q')
        if q:
            query = q.split()
            query_objects = Q()
            for part in query:
                query_objects &= Q(name__icontains=part)
            queryset = queryset.filter(query_objects)

        return queryset


class BookingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filters = {}
        fields = ['room', 'user']

        for field in fields:
            param_value = request.query_params.get(field, None)
            if param_value is not None:
                filters[f'{field}__exact'] = param_value

        start = request.query_params.get('start')
        end = request.query_params.get('end')
        if start:
            filters[f'start_time__gte'] = start
        if end:
            filters[f'end_time__lte'] = end

        q = request.query_params.get('q')
        if q:
            query = q.split()
            query_objects = Q()
            for part in query:
                query_objects &= Q(name__icontains=part)
            queryset = queryset.filter(query_objects)

        return queryset
