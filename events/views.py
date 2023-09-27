from django.shortcuts import render
from django.http import HttpResponse
# from .forms import EventsForm
from .models import Events
from django.forms import ModelForm
# Create your views here.


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = [
            "title",
            "description",
            "tags",
            "status",
            "start_date",
            "event_type",
            "creator"
        ]


def index_handler(request):
    return HttpResponse("Putting Events Here for You")


def add_events(request):
    if request.method == "GET":

        context = {
            "form":  EventsForm()
        }
        return render(request, "events/form.html", context)
    elif request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            print("The form title is ", title)
            return HttpResponse("Your form was successfully submitted")
