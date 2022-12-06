from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CHOICES
from .models import Order, Car, Comment, Message
from django.urls import reverse
from django.utils import timezone
import datetime



def index(request):
    form = CHOICES(request.POST)

    if form.is_valid():
        selected = form.cleaned_data.get("NUMS")
        print(selected)


    content = {'form': form}
    template = loader.get_template('traffic/main_page.html')
    return HttpResponse(template.render(content, request))

def commentaries(request):
    commentaries = Comment.objects.all()
    content = {"commentaries": commentaries}
    template = loader.get_template('traffic/commentaries.html')
    return HttpResponse(template.render(content, request))

def left_order(request):
    day = request.POST.get('user_profile_color_1')
    hour = request.POST.get('user_profile_color_2')
    minute = request.POST.get('user_profile_color_3')
    start = request.POST.get('start')
    finish = request.POST.get('finish')
    name = request.POST.get('input_name')
    phone = request.POST.get('input_phone')
    interest = request.POST.getlist('interest')
    form = CHOICES(request.POST)
    selected = request.POST.get("level")
    
    order = Order.objects.create(day=day, hour=hour, minute=minute, start=start, finish=finish, 
                                name=name, phone=phone, interest=interest, selected=selected)

    content = {'form': form}
    template = loader.get_template('traffic/main_page.html')
    return HttpResponse(template.render(content, request))

def cars(request):
    cars = Car.objects.all().order_by('category')

    content = {"cars": cars}
    template = loader.get_template('traffic/auto.html')
    return HttpResponse(template.render(content, request))

def left_comment(request):
    name = request.POST.get('input_name')
    text= request.POST.get('input_text')
    date = timezone.now()

    comment = Comment.objects.create(name=name, text=text, date=date)

    content = {"cars": cars}
    template = loader.get_template('traffic/auto.html')
    return redirect(reverse('commentaries'))

def contacts(request):
    content = {}
    template = loader.get_template('traffic/contacts.html')
    return HttpResponse(template.render(content, request))

def about(request):
    content = {}
    template = loader.get_template('traffic/about.html')
    return HttpResponse(template.render(content, request))

def message(request):
    content = {}
    template = loader.get_template('traffic/message.html')
    return HttpResponse(template.render(content, request))

def send_message(request):
    text = request.POST.get('message_text')
    date = timezone.now()

    message = Message(text=text, date=date)
    message.save()

    content = {}
    template = loader.get_template('traffic/message.html')
    return redirect(reverse('index'))