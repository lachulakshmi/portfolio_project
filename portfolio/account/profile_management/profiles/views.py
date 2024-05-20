from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import UserForm,ProfileForm

# Create your views here.

@login_required
def profile(request):
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=ProfileForm(request.POST,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')
    else:
        user_form=UserForm(instance=request.user)
        profile_form=ProfileForm(instance=request.user.profile)

    return render(request,'profile.html',{
        'user_form':user_form,
        'profile_form':profile_form
    })
