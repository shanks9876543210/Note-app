
from django.urls import path
from . import views
urlpatterns = [
    path('',views.NoteListCreateCon.as_view(),name="note_list"),
    path('note/<int:pk>',views.NoteView.as_view(),name="note_detail"),
]
