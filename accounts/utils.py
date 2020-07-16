from django.contrib.sites.shortcuts import get_current_site
from .tokens import confirm_email_token_generator
from django.template.loader import render_to_string


def send_confirmation_email(request, user):
    token = confirm_email_token_generator.make_token(user)
    uid = user.pk
    domain = get_current_site(request)
    print(domain)
    subject = 'Account Activation'
    context_dict = {'user': user,
                    'uid': uid,
                    'domain': domain,
                    'token': token
                    }
    message = render_to_string(
        'registration/account_activation_email.html', context_dict)

    user.email_user(subject, message)
