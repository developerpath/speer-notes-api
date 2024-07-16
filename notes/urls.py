from django.urls import path, include
from .views import NoteListCreateView, NoteDetailView, ShareNoteView

urlpatterns = [
    path('', NoteListCreateView.as_view(), name='note_list_create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/share/', ShareNoteView.as_view(), name='share_note'),
]
