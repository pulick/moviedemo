from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)

    return render(request,"detail.html",{'movie':movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES.get('img')
        # additional_img = request.FILES.get('additional_img')  # Add this line to get the additional image

        # if name:
        #     movie = Movie(name=name, desc=desc, year=year, img=img, additional_image=additional_img)
        #     movie.save()
        #     return redirect('/')
        # else:
        #     error_message = "Please provide a name for the cinema."
        #     context = {'error_message': error_message}
        #     return render(request, 'add.html', context)

    return render(request, 'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def add_additional_image(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)  # Save the form data but don't commit to the database yet
            movie.img = None  # Set the main image to None as we only want to save the additional image
            movie.save()
            return redirect('movieapp:index')  # Redirect to the home page after saving the additional image
    else:
        form = MovieForm()

    context = {'form': form}
    return render(request, 'add.html', context)

