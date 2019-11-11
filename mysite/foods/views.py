from django.shortcuts import render
from .models import Menu
from django.db.models import Q
from restaurants.models import Restaurant
# Create your views here.
def all_foods(request):
    login_user="Login"
    if request.session.get('username', None):
        login_user = request.session.get('username')

    all_Restaurant = Restaurant.objects.all()

    menus = Menu.objects.all()
    print(login_user)
    context={
        'foods':menus,
        'login_user':login_user,
        'all_Restaurant':all_Restaurant

    }
    query = request.GET.get('q')
    if query:
        menus = Menu.objects.filter(Q(name__icontains=query)).distinct()
        context = {'foods': menus}
        return render(request, 'food/index.html', context)
    return render(request,'food/index.html',context)



def all_foods_only(request):
    login_user="Login"
    if request.session.get('username', None):
        login_user = request.session.get('username')

    all_Restaurant = Restaurant.objects.all()

    menus = Menu.objects.all()
    print(login_user)
    context={
        'foods':menus,
        'login_user':login_user,
        'all_Restaurant':all_Restaurant

    }
    query = request.GET.get('q')
    if query:
        menus = Menu.objects.filter(Q(name__icontains=query)).distinct()
        context = {'foods': menus}
        return render(request, 'food/all_foods.html', context)
    return render(request,'food/all_foods.html',context)


def food_details(request,id):
    login_user = "Login"
    if request.session.get('username', None):
        login_user = request.session.get('username')

    menus = Menu.objects.get(id=id)
    menus_list = Menu.objects.all()
    context={
        'menus': menus,
        'menus_list': menus_list,
        'login_user': login_user,
    }
    return render(request,"food/details.html",context)


def res_details(request,id):
    login_user = "Login"
    if request.session.get('username', None):
        login_user = request.session.get('username')

    restaurants = Restaurant.objects.get(id=id)
    foods = Menu.objects.all()
    context={
        'foods': foods,
        'restaurants': restaurants,
        'login_user': login_user,
    }
    return render(request,"food/all_res.html",context)


