from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from  learning_python.utils import generate_confirmation_token, confirm_token

from .forms import UserLoginForm, UserRegisterForm

User = get_user_model()

def login_view(request):
	next = request.GET.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get('password')
		user = authenticate(email=email, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect("/")
	return render(request, "accounts/form.html", {"form":form, "title": title})


def register_view(request):
	next = request.GET.get('next')
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(email=user.email, password=password)
		token = generate_confirmation_token(user.email)
		confirm_url = "http://localhost:8000" + reverse("accounts:confirm_email", kwargs={"token":token})
		# confirm_url = "http://localhost:8000/accounts/confirm_email/{}".format(token)
		message = "TEST"
		html_message = render_to_string('accounts/confirm_email.html', context={"confirm_url":confirm_url})
		subject = "Please confirm your email"
		send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, html_message=html_message)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect("/")

	context = {
		"form": form,
		"title": title
	}
	return render(request, "accounts/form.html", context)

def confirm_email(request, token):
	try:
		email = confirm_token(token)
	except:
		print('The confirmation link is invalid or has expired.', 'danger')
	user = User.objects.filter(email=email).first()
	if user.is_activated:
		print('Account already confirmed. Please login.', 'success')
	else:
		user.is_activated = True
		user.save()
		print('You have confirmed your account. Thanks!', 'success')
	return render(request, "accounts/activated_email.html", {})

def logout_view(request):
	logout(request)
	return redirect("/")