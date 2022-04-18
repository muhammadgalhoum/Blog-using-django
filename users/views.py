from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserDeleteForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, (f'Your account has been updated!'), extra_tags='success')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


@login_required
def delete_user(request, uid):
    user = get_object_or_404(User, id=uid)
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=user)
        user.delete()
        messages.success(request, ('Your account has been deleted successfully.'), extra_tags='success')
        return redirect('/')
    else:
        delete_form = UserDeleteForm(instance=user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'users/delete_account.html', context)


# Types of messages in Django
'''
messages.debug
messages.info
messages.success
messages.warning
messages.error
'''

