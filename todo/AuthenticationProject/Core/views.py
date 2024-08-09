from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from email.message import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from .forms import *
from .models import *
import random
import smtplib
import ssl
import time
import hashlib


def home(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'home.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'delete.html', context)

def RegisterView(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")

        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters")

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email, 
                username=username,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')

    return render(request, 'register.html')

def LoginView(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'login.html')

def LogoutView(request):

    logout(request)
    return redirect('login')

# def ForgotPassword(request):
#     if request.method == "POST":
#         email = request.POST.get('email')

#         try:
#             user = User.objects.get(email=email)
#             reset_id = hashlib.sha256(user.email.encode()).hexdigest()

#             new_password_reset = PasswordReset(user=user, reset_id=reset_id)
#             new_password_reset.save()

#             password_reset_url = reverse('reset-password', kwargs={'reset_id': reset_id})
#             full_password_reset_url = f'{request.scheme()}://{request.get_host()}{password_reset_url}'

#             email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'
#             email_message = EmailMessage(
#                 'Reset your password',
#                 email_body,
#                 settings.EMAIL_HOST_USER,
#                 [email]
#             )

#             email_message.fail_silently = True
#             email_message.send()

#             return redirect('password-reset-sent', reset_id=reset_id)

#         except User.DoesNotExist:
#             messages.error(request, f"No user with email '{email}' found")
#             return redirect('forgot-password')

#     return render(request, 'forgot-password.html')

# def PasswordResetSent(request, reset_id):
#     if PasswordReset.objects.filter(reset_id=reset_id).exists():
#         return render(request, 'password-reset-sent.html')
#     else:
#         messages.error(request, 'Invalid reset id')
#         return redirect('forgot-password')

# def ResetPassword(request, reset_id):
#     try:
#         password_reset = PasswordReset.objects.get(reset_id=reset_id)

#         if request.method == "POST":
#             password = request.POST.get('password')
#             confirm_password = request.POST.get('confirm_password')

#             if password != confirm_password:
#                 messages.error(request, 'Passwords do not match')
#             elif len(password) < 5:
#                 messages.error(request, 'Password must be at least 5 characters long')
#             elif timezone.now() > password_reset.created_when + timezone.timedelta(minutes=10):
#                 messages.error(request, 'Reset link has expired')
#                 password_reset.delete()
#             else:
#                 user = password_reset.user
#                 user.set_password(password)
#                 user.save()
#                 password_reset.delete()
#                 messages.success(request, 'Password reset. Proceed to login')
#                 return redirect('login')

#         return redirect('reset-password', reset_id=reset_id)

#     except PasswordReset.DoesNotExist:
#         messages.error(request, 'Invalid reset id')
#         return redirect('forgot-password')

#     return render(request, 'reset_password.html')

# def generate_code(length=6):
#     return ''.join(random.choices('0123456789', k=length))


# def send_email(receiver, code):
#     sender = myemailaddress
#     password = myapppassword
#     subject = "2-step code"

#     email = EmailMessage()
#     email['From'] = sender
#     email['To'] = receiver
#     email['Subject'] = subject
#     email.set_content(f"""
#     Dear User,

#     Welcome to ToDo, your ultimate platform for organizing and managing your daily plans and tasks. We are thrilled to have you join our community!

#     At ToDo, we strive to provide you with the best tools to streamline your productivity and help you stay on top of your schedule. Whether you're planning your day, setting reminders, or tracking your goals, our site is designed to make your life easier and more organized.

#     As part of our commitment to ensuring the security of your account, we require a verification process. Below, you'll find your unique verification code. Please enter this code on the verification page to complete your registration process.

#     Your verification code is: {code}

#     If you did not request this email or if you encounter any issues, please contact our support team immediately. We are here to help you every step of the way.

#     Thank you for choosing ToDo. We look forward to helping you achieve your goals and manage your plans effectively.

#     Best Regards,
#     The ToDo Team
#     """)

#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(sender, password)
#         smtp.sendmail(sender, receiver, email.as_string())
#         print(f"Sent email to {receiver}")


# @login_required
# def TwoStepVerification(request):
#     if request.method == "POST":
#         email = request.user.email
#         code = generate_code()
#         send_email(email, code)
#         messages.success(request, "Verification code sent to your email")
#         return redirect('home')

#     return render(request, 'two_step_verification.html')

# # def true_2step_enter():
# #     if 

