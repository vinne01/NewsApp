from django.shortcuts import render
#import Tweet from models and tweetform form form
from .models import Tweet
from .forms import  TweetForm,UserRegistrationForm
from django.shortcuts import get_list_or_404,redirect,get_object_or_404
#decorate help to prevent from login only login user edit or delete or update
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
#for sending gmail import library
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from datetime import datetime


# Create your views here.
def index(request):
    return render(request,'index.html')
#search news by date and desc of news
def tweet_list(request):
    query = request.GET.get('search', '')
    date_filter = request.GET.get('date', '')  # Get the date filter from query parameters

    if date_filter:
        try:
            filter_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
            tweets = Tweet.objects.filter(
                Q(text__icontains=query),
                created_at__date=filter_date
            ).order_by('-created_at')
        except ValueError:
            tweets = Tweet.objects.filter(Q(text__icontains=query)).order_by('-created_at')
    else:
        tweets = Tweet.objects.filter(Q(text__icontains=query)).order_by('-created_at')
    
    return render(request, 'tweet_list.html', {'tweets': tweets})

def about(request):
    return render(request,'about.html')

#logic for sends emails
def index(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        class_name = request.POST.get('class')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Construct the email message
        full_message = f"Name: {name}\nClass: {class_name}\nSubject: {subject}\n\nMessage:\n{message}"
        
        # Send the email
        send_mail(
            subject,               # Subject of the email
            full_message,          # Message body
            settings.EMAIL_HOST_USER,  # From email
            ['vku563786@gmail.com'],   # Recipient list
            fail_silently=False
        )
    
    return render(request, 'emailform.html')
# def detail(request):
#     return render(request,'#')
def newsdetail(request,slug):
    newsdetail=Tweet.objects.get(slug=slug)
    data={
        'newsdetail':newsdetail
    }
    
    return render(request,'newsdetail.html',data)
       

        
     
      
      
