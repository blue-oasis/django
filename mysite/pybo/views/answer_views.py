from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """pybo 답변 등록"""
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
            #return redirect('pybo/detail', question_id=question.id) /쓰면 고장남
            #경로 / , urls name 사용 app_name:name

    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    #if else 영역 주의
    #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """pybo 답변 수정"""
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer) #답변 수정 화면에 기존 제목, 내용 반영
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now() #수정일시 저장
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(requset, answer_id):
    """pybo 답변 삭제"""
    answer = get_object_or_404(Answer, pk=answer_id)
    if requset.user != answer.author:
        messages.error(requset, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)