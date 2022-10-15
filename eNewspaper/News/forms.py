from django import forms
from django.forms import widgets
from .models import Topic,Reporter,News

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ("date","slug")
        widgets = {
            "title":widgets.TextInput(attrs={"class":"form-control"}),
            "subtitle":widgets.TextInput(attrs={"class":"form-control"}),
            "details":widgets.Textarea(attrs={"class":"form-control"}),
            "image":widgets.FileInput(attrs={"class":"form-control"}),
            "topics":widgets.SelectMultiple(attrs={"class":"form-control"}, choices=Topic.objects.all()),
            "reporter":widgets.SelectMultiple(attrs={"class":"form-control"}, choices=Reporter.objects.all()),
        }

class ReporterCreateForm(forms.ModelForm):
    class Meta:
        model = Reporter
        exclude = ("slug",)
        widgets = {
            "first_name":widgets.TextInput(attrs={"class":"form-control"}),
            "last_name":widgets.TextInput(attrs={"class":"form-control"}),
            "image":widgets.FileInput(attrs={"class":"form-control"}),
            "biography":widgets.Textarea(attrs={"class":"form-control"})
        }

class TopicCreateForm(forms.ModelForm):
    class Meta: 
        model = Topic
        exclude = ("slug",)
        widgets = {
            "topic_name":widgets.TextInput(attrs={"class":"form-control"}),
        }