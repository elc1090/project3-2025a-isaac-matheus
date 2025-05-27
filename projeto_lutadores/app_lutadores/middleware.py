from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_view = resolve(request.path_info).url_name
        exempt_views = ['login', 'logout']  # nomes das views isentas

        if not request.session.get('usuario_id') and current_view not in exempt_views:
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
