from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note, User
from .serializers import NoteSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(Q(owner=self.request.user) | Q(shared_with=self.request.user))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(Q(owner=self.request.user) | Q(shared_with=self.request.user))
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ShareNoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        note = get_object_or_404(Note, pk=pk, owner=request.user)
        username = request.data.get('username', None)

        success_message = None
        error_message = None

        try:
            shared_with_user = User.objects.get(username=username)
            if shared_with_user == request.user:
                error_message = "You cannot share a note with yourself."

            if shared_with_user in note.shared_with.all():
                error_message = f"Note is already shared with user '{username}'."

            if not error_message:
                note.shared_with.add(shared_with_user)
                success_message = f"Note shared successfully with user '{username}'."
        except User.DoesNotExist:
            error_message = f"User '{username}' does not exist."
        
        if success_message:
            return Response({"success": success_message}, status=status.HTTP_200_OK)
        else:
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

class SearchNotesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            notes = Note.objects.filter(
                Q(owner=request.user) | Q(shared_with=request.user),
                Q(title__icontains=query) | Q(body__icontains=query)
            )
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)
        else:
            return Response([])
