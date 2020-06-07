from django.contrib import admin
from django.urls import path
from report.views import IndexView

app_name = "report"

urlpatterns = [
    path('', IndexView, name='index'),

]
