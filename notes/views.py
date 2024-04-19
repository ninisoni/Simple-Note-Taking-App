from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})

def view_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/view_note.html', {'note': note})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'notes/delete_note.html', {'note': note})
