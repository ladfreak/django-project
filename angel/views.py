from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import *
from . forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
import json

def home(request):
    products = product.objects.filter(treanding=1)
    categories = catagory.objects.name
    return render(request, 'home.html',{"products":products,"catagories":categories})

def myregister(request):
    if request.method == 'POST':
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 == password2:            
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            messages.success(request,'Account created successfuly')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong in your details')
            return redirect('register')
    else:
        form = createuser()
        return render(request, "register.html", {'form': form}) 
    
   
def categories(request):
    catagories=catagory.objects.filter(status=0)
    return render(request,'categories.html',{"catagories":catagories})

def home1(request):
    return redirect('home')

def info(request):
    return render(request,'info.html')


def collection(request,name):
    if (catagory.objects.filter(name=name,status=0)):
        products=product.objects.filter(catagory__name=name)
        return render(request,'web/index.html',{"products":products,"catagory_name":name})
    else:
        messages.warning(request,"no such catagory is found")
        return redirect('catagories')
    

@authenticate
def logout(request):
    
    return render(request,'logout.html')


def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty = (data['product_qty'])
            product_id = (data['pid'])
            #print(request.user.id)
            product_status=product.objects.get(id=product_id)
            if product_status:
                if cart.objects.filter(user_id=request.user.id,product=product_id):
                    return JsonResponse({'status':'product already in cart'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        cart.objects.create(user=request.user,product_id=product_id,product_quantity=product_qty)
                        return JsonResponse({'status':'product added to cart'},status=200)
                    else:
                        return JsonResponse({'status':'product stock not available'},status=200)
        else:
            return JsonResponse({'status':'login to add cart'},status=200)
        
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def product_details(request,cname,pname):
    if (catagory.objects.filter(name=cname,status=0)):
        if (product.objects.filter(name=pname,status=0)):
            products = product.objects.filter(name=pname,status=0).first()
            return render(request,'web/product_details.html',{"products":products,"cname":cname})
        else:
            messages.error(request,"no such product not found")
            return render(request,'web/product_details.html')
    else:
        messages.error(request,"no such catagory found")
        return redirect('catagories')

def cart_page(request):
    if request.user.is_authenticated:
        carts=cart.objects.filter(user=request.user)
        return render(request,'cart.html',{'cart':carts})
    else:
        return redirect('login')
    
def cart_remove(equest,cid):
    remove=cart.objects.get(id=cid)
    remove.delete()
    return redirect('cart')

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id = (data['pid'])
            product_status=product.objects.get(id=product_id)
            if product_status:
                if fav.objects.filter(user_id=request.user.id,product=product_id):
                    return JsonResponse({'status':'product already in Favourite'},status=200)
                else:
                    fav.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added to favourite'},status=200)
        else:
            return JsonResponse({'status':'login to add favourite'},status=200)
        
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    
def favourite(request):
    if request.user.is_authenticated:
        favourite=fav.objects.filter(user=request.user)
        return render(request,'fav.html',{'fav':favourite})
    else:
        return redirect('login')    

def fav_remove(request,cid):
    remove=fav.objects.get(id=cid)
    remove.delete()
    return render(request,'fav.html')