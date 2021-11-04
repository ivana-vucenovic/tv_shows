from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index(request):
    shows = Show.objects.all()
    context ={
        'shows': shows
    }
    print(shows)
    return render(request, 'tv_show.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/show/new')
    new_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect(f'/show/{new_show.id}')

def back(request):
    return redirect('/shows')

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/show/{show.id}/update')
    to_update = Show.objects.get(id=show_id)
    
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()
   
    return redirect(f'/show/{to_update.id}')

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)

    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    obj = Show.objects.get(id=show_id)
    if request.method =="GET":
        obj.delete()
        return redirect("/")
    return redirect('/shows')

# def err(request, show_id):
#     errors = Show.objects.basic_validator(request.POST)
#     if len(errors) > 0:
#         for key,value in errors.items():
#             messages.error(request, value)
#         return redirect('/')
#     # else:
    #     show = Show.objects.get(id=id)
    #     show.title = request.POST['show.title']
    #     show.network = request.POST['show.network']
    #     show.description = request.POST['show.description']
    #     show.save()
    #     return redirect('/shows')

