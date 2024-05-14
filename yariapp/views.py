
from django.shortcuts import get_object_or_404, render,redirect,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from .models import Babyform
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
# landing_page/views.py


def logout_page(request):
    logout(request)
    return redirect('/')
    # Redirect to a page after logout, for example, the home page


def landing_page(request):
    return render(request, 'index.html')
@login_required
def home_page(request):
    return render(request, 'home.html')


def onduty(request):
    if request.method == 'POST':
        form=AddDuty(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('onduty_list') 
    else:
        form = AddDuty()
    return render(request, 'onduty.html', {'form': form})

def onduty_list(request):
    s_onduty =OnDutyform.objects.all()
    return render(request, 'onduty_list.html', {'s_onduty': s_onduty})




# def categorystay(request):
#     categorystayform = AddCategoryStay()  
#     return render(request, 'categorystay.html', {'categorystayform': categorystayform}) 

def sitters(request):
    if request.method == 'POST':
        form=AddSitter(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('sitters_list')
    else:
       form = AddSitter()
    return render(request, 'sitters.html', {'form': form})

def sitters_list(request):
   sitters =Sittersform.objects.all() 
   return render(request, 'sitters_list.html', {'sitters': sitters})
    
   

def baby(request):
   if request.method == 'POST':
       form=AddBaby(request.POST)
       if form.is_valid():
           form.save()
           print(form)
           return redirect('baby_list')
   else:   
      form = AddBaby()
   return render (request, 'baby.html', {'form':form})

def baby_list(request):
    babies = Babyform.objects.all() 
    return render(request, 'baby_list.html', {'babies': babies})

def depature(request):
    if request.method == 'POST':
        form=AddDepature(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('depature_list')
    else:
        form = AddDepature()
    return render(request, 'depature.html',{'form':form})


def baby_page(request):
    return render(request, 'baby.html')


def arrival(request):
    if request.method == 'POST':
        form=AddArrival(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('arrival_list')
    else:
        form = AddArrival()
    return render(request, 'arrival.html',{'form':form})

def arrival_list(request):
    arrivals = Arrivalform.objects.all()
    return render(request, 'arrival_list.html',{'arrivals':arrivals})

def depature_list(request):
    depatures = Depatureform.objects.all()
    return render(request, 'depature_list.html',{'depatures':depatures})

def payment(request):
    if request.method == 'POST':
        form=AddPayment(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('payment_list')
    else:
        form = AddPayment()
    return render(request, 'payment.html',{'form':form})

def payment_list(request):
    payment = Paymentform.objects.all()
    return render(request, 'payment_list.html',{'payment':payment})

def payment_page(request):
    return render(request, 'payment.html')


def payform(request):
    if request.method == 'POST':
        form=AddPayform(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('s_payment_list')
    else:
        form = AddPayform()
    return render(request, 'pay.html',{'form':form})

def sitters_payment_list(request):
    s_payment_list = Payform.objects.all()
    return render(request,'s_payment_list.html',{'s_payment_list':s_payment_list})


def dollshop(request):
    if request.method == 'POST':
        form = AddShop(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shop_list') 
    else:
        form = AddShop()
    return render(request, 'shop.html', {'form': form})


def shop_list(request):
    shop = Shopform.objects.all()
    return render(request,'shop_list.html',{'shop':shop})

def pro(request):
    if request.method == 'POST':
        form=AddProform(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('pro_list')
    else:
        form = AddProform()
        return render(request, 'procurement.html',{'form':form})


def pro_list(request):
    pro = Proform.objects.all()
    return render(request,'pro_list.html',{'pro':pro})




def baby_edit(request, id):  
    baby = get_object_or_404(Babyform, id=id)  
    if request.method == 'POST':
       form = AddBaby(request.POST, instance=baby)  
       if form.is_valid():
           form.save()
           return redirect(baby_list) 
    else:
        form = AddBaby(instance=baby)
    return render(request, 'baby edit.html', {'form': form, 'baby': baby})