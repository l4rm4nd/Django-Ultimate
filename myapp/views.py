import os, base64, io, json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Q
from django.db.models import Sum
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

@require_GET
def post_logout(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'registration/post-logout.html')

@require_GET
@login_required
def dashboard(request):
    user = request.user
    #total_items = Example.objects.filter(user=user,).count()
    total_items = 5

    context = {
        'total_items': total_items,
    }
    
    return render(request, 'dashboard.html', context)