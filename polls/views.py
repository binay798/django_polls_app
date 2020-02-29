from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Polls
# Create your views here.
def index(request):
    polls = Polls.objects.order_by('-date')
    context = {'polls':polls}
    return render(request,'polls/index.html',context)


def create(request):
    if request.method == 'POST':
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']

        poll = Polls.objects.create(question=question,option_one=option1,option_two=option2,option_three=option3)
        poll.save()
        return redirect('/')
    else:
        
        return render(request,'polls/create.html')


def vote(request,poll_id):
    poll = Polls.objects.get(id=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option_1':
            poll.option_one_count += 1
        elif selected_option == 'option_2':
            poll.option_two_count += 1
        elif selected_option == 'option_3':
            poll.option_three_count += 1
        else:
            return HttpResponse("invalid")
        poll.save()
        return redirect("polls:result",poll.id)

    else:
        
        context = {'poll':poll}
        return render(request,"polls/view.html",context)

def result(request,poll_id):
    poll = Polls.objects.get(id=poll_id)
    context = {'poll':poll}
    return render(request,'polls/result.html',context)