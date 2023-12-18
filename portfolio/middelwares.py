from django.shortcuts import HttpResponse, render
from django.conf import settings


class CustomSecurityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            path = str(request.path).split('/')
            if not 'admin2024' in path:
                if not 'uploads' in path:
                    if not 'static' in path:
                        if not request.headers.get('decoader772') == settings.ALLOWED_HEADER_FOR_FRONTEND:
                            return render(request, 'error.html')
            if response.status_code == 404:
                return render(request, 'error.html')
            return response
        except Exception as e:
            return HttpResponse(f'Something Wrong {e}')
