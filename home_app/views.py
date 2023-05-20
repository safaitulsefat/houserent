from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'Components/AboutUspage.html')


def contact(request):
    if request.method == "POST":
       email=request.POST["email"]
       message=request.POST["message"]
       name=request.POST["name"]
         
       try:
             send_mail(
      'Contact Form',
       f'From :{email}\n and Name : {name}\n'
       +message,
     'mw0641295@gmail.com',
     ['saiftasnim2002@gmail.com'],
       fail_silently=False,
     ) 
            
             messages.success(request,"Message send successfully!!....")
       except:
           messages.error(request, "Email send Failed")

       return render(request, 'Components/Contactuspage.html')
    return render(request, 'Components/Contactuspage.html')


def featured(request):
    return render(request, 'Components/FeaturedPage.html')



