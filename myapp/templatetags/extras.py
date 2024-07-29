import os
from django import template
from django.conf import settings
from django.utils.html import escape

register = template.Library()

@register.filter
def env(key):
    if key == "OIDC_ENABLED":
        return settings.OIDC_ENABLED