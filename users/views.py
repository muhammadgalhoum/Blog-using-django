from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *


def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      group = Group.objects.get(name="visitor")
      user.groups.add(group)
      messages.success(
        request, f'{username}, your account has been created Succssfully! You are now able to Log in')
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