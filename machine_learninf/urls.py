from django.urls import path
from . import views

urlpatterns=[
    path('m',views.machine),
    path('s',views.supervised),
    path('d',views.DT),
]