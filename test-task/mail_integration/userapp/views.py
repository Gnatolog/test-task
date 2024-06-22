from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm, UserLogin
import logging

logger = logging.getLogger(__name__)


class StartPageView(View):

    def get(self, request):
        return render(request, 'base.html')




def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            logger.info(f'{new_user.username} зарегистрировался')
            return render(request,
                          'userapp/template/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'userapp/template/register.html',
                  {'user_form': user_form})
