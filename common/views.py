from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

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

def update(request):
    # 회원 정보 수정
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserChangeForm(instance = request.user)

    return render(request, 'common/update.html', {'form': form})

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/password.html', {'form': form})

def page_not_found(request, exception):
    # 오류 페이지 - 404 not found
    return render(request, 'common/404.html', {})