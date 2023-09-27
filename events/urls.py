from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.index_handler, name="event_index"),
    path("create/", views.add_events, name="add_events")
]
