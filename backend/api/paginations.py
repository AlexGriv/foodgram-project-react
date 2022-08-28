from rest_framework.pagination import PageNumberPagination


class NewPagePagination(PageNumberPagination):
    page_size_query_param = 'limit'
