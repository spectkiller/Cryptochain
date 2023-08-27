from django.shortcuts import render, redirect
from json import load
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
from django.core.mail import send_mail


# Create your views here.



def index(request):
    member = Members.objects.all().values()

    template = loader.get_template("index.html")

    context = {

        "member": member

    }
    return HttpResponse(template.render(context, request))



def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST ["first"]
    y = request.POST ["last"]
    member = Members(Cryptocurrency=x, Amount=y)
    member.save()
    return HttpResponseRedirect(reverse("index"))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

    
def update(request, id):
    member=Members.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'member':member,
    }
    return HttpResponse(template.render(context,request))


def updaterecord(request, id):
    first=request.POST['first']
    last=request.POST['last']
    member=Members.objects.get(id=id)
    member.Cryptocurrency=first
    member.Amount=last
    member.save()
    return HttpResponseRedirect(reverse('index'))

def send_email(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        feedback_choice = request.POST.get('feedback')
        message = request.POST.get('message')
        sender_email = request.POST.get('email')
        subject = "Feedback"
        recipient_email = 'rajhrishabh892@gmail.com'
        full_message = f"First Name: {first_name}\nLast Name: {last_name}\nFeedback Choice: {feedback_choice}\nMessage: {message}"
        send_mail(subject, full_message, sender_email, [recipient_email])
        return render(request, 'success.html')
    return render(request,'pjkt3.html')


def pjkt4(request):
    return render(request,'pjkt4.html')

def pjkt1(request):
    return render(request,'pjkt1.html')

def pjkt2(request):
    return render(request,'pjkt2.html')


def send_email1(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        feedback_choice = request.POST.get('feedback')
        message = request.POST.get('message')
        sender_email = request.POST.get('email')
        subject = "Feedback"
        recipient_email = 'rajhrishabh892@gmail.com'
        full_message = f"First Name: {first_name}\nLast Name: {last_name}\nFeedback Choice: {feedback_choice}\nMessage: {message}"
        send_mail(subject, full_message, sender_email, [recipient_email])
        return render(request, 'success.html')
    return render(request,'pjkt3-dark.html')


def pjkt4_dark(request):
    return render(request,'pjkt4-dark.html')

def pjkt1_dark(request):
    return render(request,'pjkt1-dark.html')

def pjkt2_dark(request):
    return render(request,'pjkt2-dark.html')

def login(request):
    return render(request,'login.html')