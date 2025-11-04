from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/success.html', {'message': 'Registered Successfully!'})
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
