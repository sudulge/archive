from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'archive/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'archive/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #방법 1
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #방법 2
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()
    return redirect('archive:detail', question_id=question.id)

    