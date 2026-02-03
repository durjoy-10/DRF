from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param ='page_size'  # Allow client to set the page size using 'page_size' query parameter
    page_query_param ='page_num'        # Allow client to set the page number using 'page_num' query parameter
    max_page_size =1               # Set maximum page size to 1
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page.paginator.per_page,
            'results': data
        })