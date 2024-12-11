from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie


def home(request):
    return render(request,  'index.html')


def movie_list(request):
    movies = Movie.objects.all()
    return render (request , 'movies/movie_list.html',
                   {'movies':movies})


def movie_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        if (title and director and
                year and  genre):
            Movie.objects.create(
                title=title,
                director=director,
                year=year,
                genre=genre,
            )
            return redirect('movies:movie_list')
    return render(request, 'movies/movie_form.html')

def movie_detail(request, movie_id):
   movie = get_object_or_404(Movie, pk=movie_id)
    ctx = {'movies': movie}
    return render(request, 'contacts/detail.html', ctx)



def movie_delete(request, contact_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('movie:list')



def movie_update(request, contact_id):
    movie = get_object_or_404(Movie, pk=movies_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        if (title and director and
                year and genre):
            movie.title = title
            movie.director = director
            movie.year = year
            movie.genre = genre
            movie.save()
            return redirect(movie.get_detail_url())
    ctx = {'movie':movie}
    return render(request, 'movies/form.html', ctx)


