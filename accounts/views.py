from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Customer


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            clean_address = form.cleaned_data['address']
            user = form.save(commit=False)
            user.save()
            Customer.objects.create(user=user, address=clean_address)
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)
