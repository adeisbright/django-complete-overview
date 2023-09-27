from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # path("", views.index, name="polls_index"),
    path("", views.IndexView.as_view(), name="polls_index"),
    path("forms/", views.get_name, name="name_form"),
    path("users/authenticate/", views.authenticate_user, name="users_authenticate"),
    path("users/login", views.view_login, name="user_login"),
    path("users/logout", views.handle_logout, name="user_logout"),
    path("users/create-account", views.register_user, name="poll_create_user"),
    path("users/register", views.add_user, name="poll_users"),
    path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="result"),
    # path("<int:question_id>/results/", views.result, name="result"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("questions/", views.question_page, name="question")
]
