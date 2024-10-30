# middleware.py

from django.utils.deprecation import MiddlewareMixin

class AllowMediaIframeMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/uploads/') and request.path.endswith('.pdf'):
            response['X-Frame-Options'] = 'ALLOWALL'
        return response
