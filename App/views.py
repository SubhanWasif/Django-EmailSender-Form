from django.shortcuts import render , redirect
from .form import Contactform
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.



def index(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        email = request.POST.get('email') 
        if form.is_valid():
            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
            )
            return redirect('success')
    else:
        form = Contactform()
        return render(request, "HTML/form.html",{'form':form})
        
def success(request):
    return render(request, 'HTML/success.html',{})