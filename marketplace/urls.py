
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='designers/', permanent=False)),
    path('designers/', views.designer_list, name='designer_list'),
     path('projects/', views.project_list, name='project_list'),
    # other paths
]
 
from django.urls import path
from . import views

urlpatterns = [
    path('designer-dashboard/', views.designer_dashboard, name='designer_dashboard'),
    path('client-dashboard/', views.client_dashboard, name='client_dashboard'),
]

urlpatterns = [
    path('send-message/', views.send_message, name='send_message'),
    path('message-list/', views.message_list, name='message_list'),
]

from .views import CreateCheckoutSessionView

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
urlpatterns = [
    path('designer-profile/<str:username>/', views.designer_profile, name='designer_profile'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('designers/', views.designer_list, name='designer_list'),
    path('projects/', views.project_list, name='project_list'),
]


from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', RedirectView.as_view(url='designers/', permanent=False)),
    path('designers/', views.designer_list, name='designer_list'),
     path('projects/', views.project_list, name='project_list'),
    path('designer-dashboard/', views.designer_dashboard, name='designer_dashboard'),
    path('client-dashboard/', views.client_dashboard, name='client_dashboard'),
    path('send-message/', views.send_message, name='send_message'),
    path('message-list/', views.message_list, name='message_list'),
]
from .views import CreateCheckoutSessionView
urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('designer-profile/<str:username>/', views.designer_profile, name='designer_profile'),
    path('', views.home, name='home'),
    path('designers/', views.designer_list, name='designer_list'),
    path('projects/', views.project_list, name='project_list'),
]

 