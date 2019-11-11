from django.shortcuts import render,redirect
from foods.models import Menu
from . models import Kart,KartFood
from Accounts.forms import UserForm,LoginForm
# Create your views here.
def food_cart(request,id):
    total=0
    dish_qty = 1
    kart_done = ''
    if request.method == 'POST':

        dish_qty = request.POST['dish_qty']
        dish_name = request.POST['dish_name']
        dish_price = request.POST['dish_price']
        print(dish_qty,dish_name,dish_price)

        newqty=int(dish_qty)
        total=(float(dish_price)*int(dish_qty))

        form = KartFood(dish_name=dish_name,dish_price=total,dish_qty=newqty)
        form.save()
        kart_done = 'Yes'





    dish = Menu.objects.get(id=id)
    context = {
        'dish':dish,
        'total':total,
        'dish_qty':dish_qty,
        'kart_done':kart_done
    }

    return render(request,"kart/kart.html",context)

def withlist(request,id):
    food = KartFood.objects.all()
    total=0.00
    for f in food:

        total=total+float(f.dish_price)
    print(total)
    context = {
        'foods':food,
        'total':total
    }

    return render(request, "kart/withlist.html",context)

def delete_food(request,id):

    food = KartFood.objects.get(id=id)
    if request.method=='POST':
        food.delete()
        return redirect('withlist_kart')
    context={
        'food': food
    }
    return render(request, 'kart/confirm_delete.html',context)

def checkout(request,id):
    ragister_form=UserForm()
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    context={
        'ragister_form':ragister_form,

    }

    return render(request, 'kart/checkout.html',context)

def payment(request,id):
    return render(request, 'kart/payment.html')