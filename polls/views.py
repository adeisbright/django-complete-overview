from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Working with users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect("polls:user_login")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "polls/name.html", {"form": form})
# Create your views here.

# The user pass test conducts a test on the logged in user before moving them
# to the route of choice


def email_check(user):
    return user.email.endswith("@example.com")


def index(request):
    template = loader.get_template("polls/index.html")
    context = {
        "colors": ["Blue", "Green", "Red"],
        "is_valid": True,
        "name": "Jonathan Messiah",
        "message": "We have been talking about the possibility of a military confrontation",
        "blog_entries": [
            {
                "title": "Hired by MFS Africa as a Backend Developer",
                "body": "I am hoping to get a job at MFS as a backend Developer"
            }
        ]
    }

    return render(request, "polls/child.html", context)


def question_page(request):
    latest_questions = Question.objects.order_by("pub_date")[:5]

    context = {
        "latest_questions": latest_questions
    }

    return render(request, "polls/question.html", context)


@login_required
@user_passes_test(email_check)
def detail(request, question_id):
    # if not request.user.is_authenticated:
    #     return redirect("polls:user_login")
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")
    # return HttpResponse('You are viewing question %s' % question)
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})


def result(request, question_id):
    # response = "This is the result page for question %s"
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            "question": question,
            "error_message": "You did not select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        ''' Return the last five published questions '''
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):

    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def add_user(request):
    try:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstName = request.POST["firstname"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=firstName
        )
        return HttpResponse("The user was created successfully", status_code=200)
    except KeyError as error:
        print(error)
        return HttpResponse(error)


def register_user(request):
    return render(request, "polls/register.html")


def update_password_handler(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.get(username=username)
        if user is not None:
            user.set_password(password)
            user.save()
            return HttpResponse("Password updated")
        else:
            return HttpResponse("Password not updated")
    except KeyError as error:
        print(error)
        return HttpResponse(error)


def update_password(request):
    return render(request, "polls/password-update.html")


def authenticate_user(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]  # "12345678abcdABCD"
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend=None)

            return HttpResponse("Login successful")
        else:
            return HttpResponse("Login is not successful")
    except KeyError as error:
        print(error)
        return HttpResponse("Please, fill the form correctly")


def view_login(request):
    return render(request, "polls/login.html")


def handle_logout(request):
    logout(request)
    return redirect("polls:user_login")
