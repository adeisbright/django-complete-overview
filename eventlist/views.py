from django.http import HttpResponse


def handler404(request, exception):
    return HttpResponse("Sorry, we could not find what you are looking for")
