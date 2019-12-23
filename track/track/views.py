from django.shortcuts import render  
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import UserCreationForm  
from django.contrib.auth import views as auth_views     

def index(request):

    context ={
      'judul':'Home',
      'webname': 'Brand Name',
    }

    if request.user.is_authenticated:
        print('sss')
    else:
        print('ssaaas')
        return redirect("login")
    
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm

    context={
        'form': form,
    }

    
    return render(request, "main/register.html", context)