"""medica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from inventory.views import HospitalListView
from inventory.views import AdminRegistrationView
from inventory import views

urlpatterns = [
    path('stats/', views.StatsView, name="stats"),
    path('admin/', admin.site.urls),
    path('officials/', HospitalListView.as_view(),
        name='hospital_list'),
    path('hospital/', include('inventory.urls')),
    path('admin/register/', AdminRegistrationView.as_view(),
        name='admin_register'),
]
