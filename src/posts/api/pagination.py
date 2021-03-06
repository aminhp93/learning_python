from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class PostPageNumberPagination(PageNumberPagination):
	page_size = 3
	page_size_query_param = 'page_size'
	max_page_size = 10000

class PostLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 3
	max_limit = 10