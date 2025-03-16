# note/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.urls import reverse

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # created_at у нас auto_now_add, так что мы не задаём здесь
        note = Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'note/note_create.html')

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_detail', pk=note.pk)
    return render(request, 'note/note_update.html', {'note': note})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note/note_delete.html', {'note': note})
