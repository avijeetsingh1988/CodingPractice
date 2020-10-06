from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {'Author': 'AviG',
    'Title': 'Post 1',
    'Content': 'Post 1 Content',
    'Date_Posted': 'Today'
    },
    {'Author': 'John Doe',
    'Title': 'Post 2',
    'Content': 'Post 2 Content',
    'Date_Posted': 'Today'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')

# Create your views here.
