from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/details.html', {'question': question})    


def votes(request, question_id):
    # return HttpResponse("you are looking at votes of questioin %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myapp:result', args=(question.id,)))

def results(request, question_id): 
    result = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/results.html', {'result': result})    
    # return HttpResponse("you are looking at results of questioin %s" %question_id)
