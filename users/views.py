import os
import requests
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, DetailView, UpdateView
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import forms, models


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back {user.email}")
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    messages.info(request, "See you later")
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.save()
    except models.User.DoesNotExist:
        pass
    return redirect(reverse("core:home"))


def kakao_login(request):
    REST_API_KEY = os.environ.get("KAKAO_KEY")
    REDIRECT_URI = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    )


class KakaoException(Exception):
    pass


def kakao_callback(request):
    client_id = os.environ.get("KAKAO_KEY")
    redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
    try:
        code = request.GET.get("code")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
        )
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException("Can't get authorization code.")
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )
        profile_json = profile_request.json()
        email = profile_json.get("kakao_account").get("email", None)
        if email is None:
            raise KakaoException("Please also give me your email.")
        try:
            user = models.User.objects.get(email=email)
            if user.login_method != models.User.LOGIN_KAKAO:
                raise KakaoException("Please login with: {{user.login_method}}")
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                username=email,
                email=email,
                login_method=models.User.LOGIN_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
        login(request, user)
        messages.success(requests, f"Welcome back {user.email}")
        return redirect(reverse("core:home"))
    except KakaoException as e:
        messages.error(requests, e)
        return redirect(reverse("users:login"))


class UserProfileView(DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(UpdateView):

    model = models.User
    template_name = "users/update-profile.html"
    fields = ("name",)

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(PasswordChangeView):
    template_name = "users/update-password.html"
