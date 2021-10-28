from django.shortcuts import render, redirect
from . models import Show

# def index(request):
#     return render(request, 'tv_show.html')

def new(request):
    if request.method == 'GET':   
        return render(request, 'new.html')
    if request.method == 'POST':
        print(request.POST)
        return redirect('/shows')

def edit(request, show_id):
    if request.method == 'GET':
        return render(request, 'edit.html')
    if request.method == 'POST':
        return 

# def show(request, show_id):
#     return render(request, 'show.html')

def index(request):
    shows = Show.objects.all()
    context ={
        'shows': shows
    }
    print(shows)
    return render(request, 'tv_show.html', context)

def show(request, show_id):
    # query for one show with show_id
    one_show = Show.objects.get(id=show_id)

    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)


