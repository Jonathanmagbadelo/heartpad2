from django.urls import path
from HeartPad import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('new-entry/', views.new_entry, name='new-entry'),
    path('entry-list/', views.entry_list, name='entry-list'),
]
