from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    # 계정생성
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # form.cleaned_data : 입력값을 개별적으로 얻고 싶을 때 사용
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증 (사용자명과 비밀번호가 정확한지 검증)
            login(request, user)  # 로그인
            return redirect('index')
    else:
        # get 요청일 경우 계정생성 화면 리턴
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})