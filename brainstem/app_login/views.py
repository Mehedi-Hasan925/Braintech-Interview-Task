from django.shortcuts import render,HttpResponseRedirect,redirect
from app_login import forms
from app_login import models
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    form = forms.SignupForm()
    has_error = False
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # user_profile = models.Profile(user=user)
            # print(user_profile)
            # user_profile.save()
            HttpResponseRedirect(reverse('app_login:login'))
            
    diction = {'form':form,'has_error':has_error}
    return render(request,'app_login/signup.html',context=diction)




def log_in(request):
    # form = forms.LoginForm()
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =  authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_user_activity:home'))

    diction = {'form':form}
    return render(request,'app_login/log_in.html',context=diction)


@login_required
def log_out(request):
    logout(request)
    messages.add_message(request,messages.INFO, 'Logout successfully')
    return HttpResponseRedirect(reverse('app_login:login'))



@login_required
def profile_page(request):
    
    return render(request,'app_login/profile.html')




@login_required
def Add_Profile_Info(request):
    current_user = models.Profile.objects.get(user=request.user)
    form = forms.UserProfileForm(instance=current_user)
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = forms.UserProfileForm(instance=current_user)
            return HttpResponseRedirect(reverse('app_user_activity:home'))

    diction = {'form':form}
    return render(request,'app_login/profile_info_set.html',context=diction)

@login_required
def change_profile_pic(request):
    current_user = models.Profile.objects.get(user=request.user)
    form = forms.ProfilePicChange(instance=current_user)
    if request.method == 'POST':
        form = forms.ProfilePicChange(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = forms.ProfilePicChange(instance=current_user)
            return HttpResponseRedirect(reverse('app_user_activity:home'))

    diction = {'form':form}
    return render(request,'app_login/profile_info_set.html',context=diction)



