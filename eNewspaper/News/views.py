from unittest import result
from django.shortcuts import render,redirect
from .forms import TopicCreateForm, ReporterCreateForm, NewsCreateForm
from .models import News, Reporter, Topic
from pywttr import Wttr
from datetime import datetime

# Create your views here.
def add_topic(request):
    if request.method == "POST":
        form = TopicCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
    form = TopicCreateForm()
    return render(request,"news/add_topic.html", {"form":form})

def add_reporter(request):
    if request.method == "POST":
        form = ReporterCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    form = ReporterCreateForm()
    return render(request,"news/add_reporter.html",{"form":form})

def add_news(request):
    if request.method == "POST":
        form = NewsCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    form = NewsCreateForm()
    return render(request, "news/add_news.html", {"form":form})


def news_details(request,slug):
    news = News.objects.get(slug=slug)
    bar_news = News.objects.order_by("?")
    reporters = news.reporter.all()
    return render(request, "news/news_details.html", {"news":news, "reporters":reporters, "bar_news":bar_news}) 
    
def reporter_details(request,slug):
    reporter = Reporter.objects.get(slug=slug)
    reporter_news = reporter.news.all()
    reporter_news  = reporter_news.order_by("-date")
    return render(request, "news/reporter_details.html", {"reporter":reporter, "reporter_news":reporter_news}) 
    
def get_news_by_topic(request, slug):
    topic = Topic.objects.get(slug=slug)
    list_news = topic.news.all()
    list_news = list_news.order_by("-date")
    return render(request, "news/get_news_by_topic.html", {"topic":topic, "list_news":list_news})    

def weather_forecast(request):
    cities = ["Los Angeles", "San Francisco", "New York City", "Las Vegas", "Chicago", "Boston", "Philadelphia","Dallas","Miami", "Oklahoma City", "Minneapolis","San Jose", "Houston", "Sacramento", "Louisville","Cambridge", "Cleveland", "Denver"]
    forecasts = []
    date = datetime.today()
    for city in cities:
        weather = Wttr(location=city)
        forecast = weather.en()
        forecast = forecast.weather[0].avgtemp_f
        forecasts.append(forecast) 
    weather = {
        "cities":cities,
        "forecasts" : forecasts,
        "date":date
    }
    context = {"weather":weather}
    return render(request, "news/weather_forecast.html", {"context":context})
