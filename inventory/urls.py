from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',
        views.Dashboard.as_view(),
        name='dashboard'),    

    path('state/<slug:state>/', 
        views.HospitalListView.as_view(),
        name='hospital_list_state'),
    
    path('<slug:slug>/',
        views.HospitalDetailView.as_view(),
        name='hospital_detail'),

]