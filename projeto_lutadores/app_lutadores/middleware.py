from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

EXEMPT_VIEWS = ['login', 'logout']
EXEMPT_PATH_PREFIXES = ['/static/', '/media/']

class LoginRequiredMiddleware:
    """
    Bloqueia acesso a todas as views exceto as URLs em EXEMPT_URLS.
    Redireciona para settings.LOGIN_URL se não estiver autenticado.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('usuario_id') and request.path not in EXEMPT_URLS:
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
