from django.db import transaction
from django.utils.deprecation import MiddlewareMixin


class DBTransactionMiddleware(MiddlewareMixin):
    def __call__(self, request, *args, **kwargs):
        if request.method in ('POST', 'PUT', 'DELETE'):
            with transaction.atomic():
                response = self.get_response(request)
        else:
            response = self.get_response(request)
        return response
