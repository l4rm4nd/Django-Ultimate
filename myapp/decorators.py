from django.shortcuts import redirect
from django.urls import resolve, Resolver404
from functools import wraps

def custom_decorator(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("User is not authenticated.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
