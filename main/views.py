from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import ToDo
from .models import ToMeet
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def meeting(request):
    meeting_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"meeting_list": meeting_list})


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    # print(text)
    return HttpResponse("Форма получена")
