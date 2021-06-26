from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from notes.forms import NoteForm

from notes.models import Note


class FeedView(LoginRequiredMixin, ListView):
    template_name = 'logged/notes/feed.html'
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')
    

class NewNoteView(LoginRequiredMixin, CreateView):
    template_name = "logged/notes/new_note.html"
    form_class = NoteForm
    success_url = reverse_lazy('notes:feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditNoteView(LoginRequiredMixin, UpdateView):
    template_name = 'logged/notes/new_note.html'
    form_class = NoteForm
    success_url = reverse_lazy('notes:feed')
    slug_field = 'pk'
    slug_url_kwarg = 'note_pk'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    slug_field = 'pk'
    slug_url_kwarg = 'note_pk'
    template_name = 'logged/notes/delete.html'
    success_url = reverse_lazy('notes:feed')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)
