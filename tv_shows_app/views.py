from django.shortcuts import render

# def index(request):
#     return render(request, 'tv_show.html')

def index(request):
    context ={
        'shows': Show.objects.all()
    }
    return render(request, 'tv_show.html', context)

def show(request, show_id):
    # query for one show with show_id
    one_show = Show.objects.get(id=show_id)

    context = {
        'show': one_show
    }
    return render(request, 'tv_show.html', context)

# Create your views here.
