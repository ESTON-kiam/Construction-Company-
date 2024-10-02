from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from ConstructionApp.forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def blog(request):
    return render(request, 'blog.html')


def projects(request):
    return render(request, 'projects.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # Send email to admin
            subject = f"New Contact Form Submission: {contact.subject}"
            message = f"""
            New message from {contact.name} <{contact.email}>:

            {contact.message}
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['admin@example.com'],  # Replace with your admin's email
            )
            return HttpResponse("Your message has been sent. Thank you!")
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})