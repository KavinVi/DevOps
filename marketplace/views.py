from collections import UserDict
from mailbox import Message
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Designer  # Ensure this matches your model definition


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'marketplace/register.html', {'form': form})

from django.shortcuts import render
from .models import Designer, Portfolio

def designer_list(request):
    designers = Designer.objects.all()
    return render(request, 'marketplace/designer_list.html', {'designers': designers})



def marketplace_home(request):
    return render(request, 'marketplace/homepage.html')

from django.shortcuts import render

def home(request):
    return render(request, 'marketplace/home.html')

def project_list(request):
    # Add logic to retrieve and display projects
    return render(request, 'marketplace/project_list.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project

@login_required
def designer_dashboard(request):
    projects = Project.objects.filter(designer=request.user)
    return render(request, 'marketplace/designer_dashboard.html', {'projects': projects})

@login_required
def client_dashboard(request):
    projects = Project.objects.filter(client=request.user)
    return render(request, 'marketplace/client_dashboard.html', {'projects': projects})

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver = User.objects.get(username=request.POST['receiver']) # type: ignore
        content = request.POST['content']
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('message_list')

@login_required
def message_list(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'marketplace/message_list.html', {'messages': messages})

import stripe
from django.conf import settings
from django.views import View
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Design Project Payment',
                        },
                        'unit_amount': 2000,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

def designer_profile(request, username):
    designer = User.objects.get(username=username) # type: ignore
    portfolio = Portfolio.objects.filter(designer=designer)
    return render(request, 'marketplace/designer_profile.html', {'designer': designer, 'portfolio': portfolio})

from django.shortcuts import render

def home(request):
    return render(request, 'marketplace/home.html')

def designer_list(request):
    # Your code to list designers
    return render(request, 'marketplace/designer_list.html')

def project_list(request):
    # Your code to list projects
    return render(request, 'marketplace/project_list.html')
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Profile

def designer_list(request):
    query = request.GET.get('q', '')
    skill_filter = request.GET.get('skill', '')
    location_filter = request.GET.get('location', '')
    sort_option = request.GET.get('sort', 'rating')

    designers = Profile.objects.filter(user__is_staff=False)

    if query:
        designers = designers.filter(
            Q(user__username__icontains=query) | Q(bio__icontains=query)
        )

    if skill_filter:
        designers = designers.filter(skills__name__icontains=skill_filter)

    if location_filter:
        designers = designers.filter(location__icontains=location_filter)

    if sort_option == 'rating':
        designers = designers.order_by('-rating')
    elif sort_option == 'experience':
        designers = designers.order_by('-experience')
    elif sort_option == 'availability':
        designers = designers.order_by('-availability')

    paginator = Paginator(designers, 10)  # Show 10 designers per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'designers': page_obj,
        'query': query,
        'skill_filter': skill_filter,
        'location_filter': location_filter,
        'sort_option': sort_option,
    }
    return render(request, 'marketplace/designer_list.html', context)

# marketplace/views.py

from django.shortcuts import render
from .models import Designer, Project  # Ensure models are imported correctly

def designer_list(request):
    designers = Designer.objects.all().order_by('-rating')  # Use a valid field
    return render(request, 'marketplace/designer_list.html', {'designers': designers})

from django.shortcuts import render
from .models import Project
from django.db.models import Q

def project_list(request):
    sort_option = request.GET.get('sort', 'created_at')
    filter_option = request.GET.get('filter', '')

    projects = Project.objects.all()

    if filter_option:
        projects = projects.filter(
            Q(title__icontains=filter_option) | Q(description__icontains=filter_option)
        )

    if sort_option == 'date':
        projects = projects.order_by('-created_at')
    elif sort_option == 'rating':
        projects = projects.order_by('-rating')

    context = {
        'projects': projects,
        'sort_option': sort_option,
        'filter_option': filter_option,
    }
    return render(request, 'marketplace/project_list.html', context)

from django.core.paginator import Paginator

def project_list(request):
    sort_option = request.GET.get('sort', 'created_at')
    filter_option = request.GET.get('filter', '')

    projects = Project.objects.all()

    if filter_option:
        projects = projects.filter(
            Q(title__icontains=filter_option) | Q(description__icontains=filter_option)
        )

    if sort_option == 'date':
        projects = projects.order_by('-created_at')
    elif sort_option == 'rating':
        projects = projects.order_by('-rating')

    paginator = Paginator(projects, 10)  # Show 10 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_option': sort_option,
        'filter_option': filter_option,
    }
    return render(request, 'marketplace/project_list.html', context)
