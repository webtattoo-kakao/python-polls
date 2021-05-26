from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


class ListView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question


def index(request):
    return render(request, 'polls/index.html', {
        'list': Question.objects.order_by('-pub_date')[:5]
    })

def detail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {
        'question': question_detail
    })

def vote(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    choice_value = int(request.POST['choice_id'])

    try:
        selected_choice = question_detail.choice_set.get(pk=choice_value)
        selected_choice.votes += 1
        selected_choice.save()

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question_detail,
            'error_message': "답변을 선택해 주세요.",
        })

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {
        'question': question_detail,
    })

















def index_backup3(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def index_backup2(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def index_backup(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]

    # question_text = ",".join([q.question_text for q in latest_question_list])

    question_text = "<ul>"
    for q in latest_question_list:
        question_text += "<li style='height: 40px;'><a href='#'>" + q.question_text + "</a></li>"
    question_text += "</ul>"

    page_title = "<h1> 설문을 선택해 주세요. </h1>"
    response_text = "<html><head><title>설문 목록</title></head><body>" + page_title + question_text + "</body></html>"

    return HttpResponse(response_text)



def detail_backup(request, question_id):

    """
    try:
        question_detail = Question.objects.get(pk=question_id)

    except:
        raise Http404("질문이 존재하지 않습니다.")
    """

    question_detail = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {
        'question': question_detail
    })























