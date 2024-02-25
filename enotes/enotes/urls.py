"""
URL configuration for enotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from authh.views import *
from home.views import *
from intigs.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout', Logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('addNotes', addNotes, name='addNotes'),
    path('viewNotes', viewNotes, name='viewNotes'),
    path('editNotes/<pid>', editNotes, name='editNotes'),
    path('deleteNotes/<pid>', deleteNotes, name='deleteNotes'),
    path('about', about, name='about'),
    path('contrib', contrib, name='contrib'),
    # path('razorpay-payment/', razorpay_payment, name='razorpay_payment'),
    # path('handle_razorpay_response/', handle_razorpay_response, name='handle_razorpay_response'),
    # path('paymenthandler/<razorpayEmail>', paymenthandler, name='paymenthandler'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('submit_email/', submit_email, name='submit_email'),
    path('publish_note/<int:pid>/', publish_note, name='publish_note'),
    path('unpublish_note/<int:pid>/', unpublish_note, name='unpublish_note'),
    
     path('payment_success/', payment_success, name='payment_success'),
     
    
]
urlpatterns += [
    re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name='404'),
]