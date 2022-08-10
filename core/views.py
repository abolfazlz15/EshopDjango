from urllib import request
from django.shortcuts import render
from .forms import ContactUsForm
from .models import ContactUs



def contactUsView(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
    else:
        form = ContactUsForm()


    return render(request, 'core/contact-us.html', context={'form': form})        