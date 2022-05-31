from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import *


# Index page
class IndexView(generic.ListView):  # ListView 와 DetailView 차이가 무엇인가?
    template_name = 'polls/index.html'  # 이렇게 정해진(약속된) 변수에 값을 기입해야 하는 것 같다
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()  # 생성 날짜가 지금인 것만 가져오는건가?
        ).order_by('-pub_date')[:5]


# polls/<int:pk>
class DetailView(generic.DetailView):  # DetailView
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# polls/<int:pk>/results/
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# polls/<int:question_id>/vote/
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # 존재하면 객체를 가져오고 아니면 404 에러 발생
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



