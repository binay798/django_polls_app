from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request,'polls/index.html',context)


def create(request):
    context = {}
    return render(request,'polls/create.html',context)


def view(request):
    return render(request,'polls/view.html')

def result(request):
    context = {}
    return render(request,'polls/result.html',context)