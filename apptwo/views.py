from django.shortcuts import render,redirect
from .forms import signupform
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def signup(request):
    if request.method!='POST':
        form=signupform()
    else:
        form=signupform(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect('appone:home')
    return render(request,'signup.html',{'form':form})
@method_decorator(login_required,name='dispatch')
class UpdateAccountSetting(UpdateView):
    model=User
    fields=['first_name','last_name','email']
    template_name = 'account_edit.html'
    success_url =reverse_lazy('apptwo:edit_account')
    def get_object(self, queryset=None):
        return self.request.user