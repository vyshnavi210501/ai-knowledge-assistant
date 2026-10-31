from rest_framework.pagination import PageNumberPagination


class DocumentPagination(PageNumberPagination):
    """Custom pagination class for Document model.page size is set to 2 by default, but can be overridden by providing a 'page_size'
      query parameter in the request. The maximum page size is set to 5."""
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5