import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    position = django_filters.CharFilter(field_name='position', lookup_expr='iexact')  # Enable filtering by position (case-insensitive)
    first_name= django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')  # Enable filtering by first name (contains, case-insensitive)
    # id= django_filters.RangeFilter(field_name='id')  # Enable filtering by id range
    
    id_min = django_filters.CharFilter(method='filter_by_id_range', label="From EMP ID")
    id_max = django_filters.CharFilter(method='filter_by_id_range', label="To EMP ID")
    class Meta:
        model = Employee
        # fields = ['position', 'first_name','id']  
        fields = ['position', 'first_name', 'id_min', 'id_max']  # Fields available for filtering
    
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)  # Filter IDs greater than or equal to value
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)  # Filter IDs less than or equal to value
        return queryset