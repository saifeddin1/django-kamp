from django.template.loader import render_to_string


def send_success_email(request, user, order):

    subject = 'Order Successfuly Placed'
    context = {'user': user, 'order': order}
    message = render_to_string(
        'orders/success_email.html', context)

    user.email_user(subject, message)
