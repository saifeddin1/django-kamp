from django.http.response import HttpResponseBadRequest
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import Customer
from .utils import send_confirmation_email
from.tokens import confirm_email_token_generator

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            clean_address = form.cleaned_data['address']
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            Customer.objects.create(user=user, address=clean_address)
            send_confirmation_email(request, user)
            return render(request, 'registration/signup_success.html')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


def activate_email(request, uid, token):
    user = get_object_or_404(User, pk=uid)
    if confirm_email_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('login')
    else:
        return HttpResponseBadRequest('Bad Token !')
