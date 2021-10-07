from django.shortcuts import render ,  redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserForm

def sendmail(request):

    if request.method == 'POST':

        email = request.POST['email']
        msg = request.POST['msg']
        print(email, msg)

        send_mail(
            'test',
            msg,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

    return render(request, 'one/one.html')


@login_required
def passwordChangeForm(request):
    form = PasswordChangeForm(request.user)
    return render(request, 'one/changepass.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'one/register.html', {'form': form})