from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import signUpForm, accountUpdateForm, profileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    
    if(request.method == 'POST'):
        form = signUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account had been successfully created! You can log in below.')
            return redirect('login')

    else:    
        form = signUpForm()
    
    return render(request,'account/signup.html',{'form':form})

@login_required
def profile(request):

    if request.method == 'POST':
        accUpdateForm = accountUpdateForm(request.POST, instance=request.user)
        proUpdateForm = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if accUpdateForm.is_valid() and  proUpdateForm.is_valid():
            accUpdateForm.save()
            proUpdateForm.save()
            messages.success(request, f'Your account has been successfully updated.')
            return redirect('profile')
    else:
        accUpdateForm = accountUpdateForm(instance=request.user)
        proUpdateForm = profileUpdateForm(instance=request.user.profile)

    context = {
        'accUpdateForm':accUpdateForm,
        'proUpdateForm':proUpdateForm
    }

    return render(request,'account/profile.html', context)
    