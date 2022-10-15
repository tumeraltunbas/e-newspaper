from django.contrib import admin
from .models import News, Reporter,Topic
#Register your models here.
admin.site.register(News)
admin.site.register(Reporter)
admin.site.register(Topic)
