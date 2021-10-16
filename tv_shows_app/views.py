from django.shortcuts import render

def index(request):
    return render(request, 'tv_show.html')

def show(request, show_id):
    show = Show.objects.get(id=show_id)
    context ={
        'show': show
    }
    return render(request, 'tv_show.html', context)

# Create your views here.
