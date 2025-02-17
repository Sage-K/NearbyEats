from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode 
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings

def detectUser(user):
    if user.role == 1:
        redirecturl = 'restaurantDashboard'
        return redirecturl
    elif user.role == 2:
        redirecturl = 'customerDashboard'
        return redirecturl
    elif user.role == None and user.is_superadmin:
        redirecturl = '/admin'
        return redirecturl

   
def send_verification_email(request, user, subject, email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    message = render_to_string(email_template, {
        'user': user,
        'domain': current_site,
         # Encode user ID
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    mail = EmailMessage(subject, message,from_email, to=[to_email])
    mail.send()
''' 
def send_verification_email(request, user):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        current_site = get_current_site(request).domain  # Get the domain
        subject = 'Activate Your Account'
        message = render_to_string('accounts/emails/verify_email.html', {
            'user': user,
            'domain': f"http://{current_site}" if "localhost" in current_site else f"http://{current_site}",
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),  
            'token': default_token_generator.make_token(user)
        })

        to_email = user.email
        mail = EmailMessage(subject, message, from_email, to=[to_email])
        mail.content_subtype = "html"  # Ensure HTML formatting
        mail.send()
        print(f"Verification email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")  # Print errors for debugging  
'''