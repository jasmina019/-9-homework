from django.shortcuts import render, redirect, get_object_or_404
from .models import Music



def home(request):
    return render(request, 'index.html')

def music_list(request):
    music = Music.objects.all()
    ctx = {'music': music}
    return render(request, 'music/music_list.html', ctx)


def music_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        if title and genre:
            Music.objects.create(
                title=title,
                genre=genre
            )
            return redirect('music:music_list')
    return render(request, 'music/music_form.html')


def music_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    ctx = {'music': music}
    return render(request, 'music/music_detail.html', ctx)

def music_delete(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    music.delete()
    return redirect('music:music_list')

def music_update(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        if title  and genre:
            music.title = title
            music.genre = genre
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'music/music_form.html', ctx)

