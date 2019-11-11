from django.shortcuts import render,redirect
from .models import UserProfile
from Accounts.models import NewUsers

def user_proile(request):
    if not request.session.get('username', None):
        return redirect('login')
    if request.session.get('username', None):
        user_login = 'Login'
        user_login = request.session.get('username', None)

        print(type(user_login))

        user = NewUsers.objects.get(username=user_login)
        u=user.pk
        profile = UserProfile.objects.get(pk=u)
        context={
            'profile':profile
        }
    return render(request,"profile/index.html",context)

def update_profile(request,id):
    return render(request,'profile/update_profile.html')