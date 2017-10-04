from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Horse

# Create your views here.
def index(request):
    horses = Horse.objects.all()
    return render(request, 'index.html', {'horses':horses})

def detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    return render(request, 'detail.html', {'horse': horse})

def post_horse(request):
    form = HorseForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=True)

    return HttpResponseRedirect('/')