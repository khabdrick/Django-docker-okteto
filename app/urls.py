from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_contact, name='create-items'),
    path('list/', views.ContactListView.as_view(), name='view-contacts'),]