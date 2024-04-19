from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/<int:note_id>/', views.view_note, name='view_note'),
    path('note/add/', views.add_note, name='add_note'),
    path('note/edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('note/delete/<int:note_id>/', views.delete_note, name='delete_note'),
]

