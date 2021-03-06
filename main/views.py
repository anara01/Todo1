from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ToMeet
from .models import Habits
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
    todo = ToDo(text=text)
    todo.save()
    # print(text)
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list": habits_list})
