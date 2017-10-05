from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Horse
from .forms import HorseForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    horses = Horse.objects.all()
    form = HorseForm()
    return render(request, 'index.html', {'horses':horses, 'form':form})

def detail(request, horse_id):
    horse = Horse.objects.get(id=horse_id)
    return render(request, 'detail.html', {'horse': horse})

def post_horse(request):
    form = HorseForm(request.POST, request.FILES)
    horse = form.save(commit = False)
    horse.user=request.user
    horse.save()
    if form.is_valid():
        form.save(commit=True)
     
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    horses = Horse.objects.filter(user=user)
    return render(request,'profile.html', {'username':username,'horses': horses})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and password were incorrect.")


    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_horse(request):
    horse_id = request.POST.get('horse_id', None)

    likes=0
    if (horse_id):
        horse = Horse.objects.get(id=int(horse_id))
        if horse is not None:
            likes = horse.likes + 1
            horse.likes = likes
            horse.save()
    return HttpResponse(likes)

