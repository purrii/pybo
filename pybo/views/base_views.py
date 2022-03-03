# 기본관리. index, detail

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question

def index(request):
    3/0 #강제로 오류 발생
    # pybo에서 목록이 출력되도록
    page = request.GET.get('page','1') #페이지
    kw = request.GET.get('kw','') #검색어
    so = request.GET.get('so','recent') #정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer','-create_date')
    else: #recent
        question_list = Question.objects.order_by('-create_date')

    # 조회, 검색

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw) | #질문 작성자 검색
            Q(answer__author__username__icontains=kw) | #답글 작성자 검색
            Q(answer__content__icontains=kw) #답글 내용 검색
        ).distinct() #중복 제거

    # 페이징 처리
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so}
    return render(request, 'pybo/question_list.html', context)
    # render : 파이썬 데이터를 템플릿에 적용해 HTML로 반환하는 함수

def detail(request, question_id):
    # pybo 내용 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
    # 로컬호스트/pybo/2 페이지가 요청되면 최종적으로 detail 함수의 매개변수인 question_id에는 2라는 값 전달
