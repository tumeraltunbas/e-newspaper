from django.urls import path
from . import views
urlpatterns = [
    path("add_topic", views.add_topic, name="add_topic"),
    path("add_reporter", views.add_reporter, name="add_reporter"),
    path("add_news", views.add_news, name="add_news"),
    path("weather_forecast", views.weather_forecast, name="weather_forecast"),
    path("topics/<slug:slug>", views.get_news_by_topic, name="get_news_by_topic"),
    path("reporters/<slug:slug>", views.reporter_details, name="reporter_details"),
    path("<slug:slug>", views.news_details, name="news_details")
]