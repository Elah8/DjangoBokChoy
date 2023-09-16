from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name'] 
        message_email = request.POST['message-name'] 
        message = request.POST['message']

        # send an email
        send_mail(
            message_name, # subject
            message, # message
            ['Email@gmail.com', '2ndEmail@gmail.com'], # To Email
        ) 


        return render(request, 'contact.html', {'message_name': message_name})
    
    else:
        return render(request, 'contact.html', {})


def hours(request):
    return render(request, 'hours.html', {})

def service(request):
    return render(request, 'service.html', {})

def fees(request):
    return render(request, 'fees.html', {})

def downloadable(request):
    return render(request, 'downloadable.html', {})

def policies(request):
    return render(request, 'policies.html', {})

def resources(request):
    return render(request, 'resources.html', {})

def clinicNews(request):
    return render(request, 'clinicNews.html', {})

def faqs(request):
    return render(request, 'faqs.html', {})


def about(request):
    return render(request, 'about.html', {})







def appointment(request):
    if request.method == 'POST':
        '''
        message_name = request.POST['message-name'] 
        message_email = request.POST['message-name'] 
        message = request.POST['message']
'''
        # send an email
        '''
        send_mail(
            message_name, # subject
            message, # message
            ['Email@gmail.com', '2ndEmail@gmail.com'], # To Email
        ) 
        '''


        return render(request, 'appointment.html', {})
    
    else:
        return render(request, 'home.html', {})
    




