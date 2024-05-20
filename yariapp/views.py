
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

@login_required
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

@login_required
def onduty_list(request):
    s_onduty =OnDutyform.objects.all()
    return render(request, 'onduty_list.html', {'s_onduty': s_onduty})




# def categorystay(request):
#     categorystayform = AddCategoryStay()  
#     return render(request, 'categorystay.html', {'categorystayform': categorystayform}) 
@login_required
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

@login_required
def sitters_list(request):
   sitters =Sittersform.objects.all() 
   return render(request, 'sitters_list.html', {'sitters': sitters})
    
   
@login_required
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

@login_required
def baby_list(request):
    babies = Babyform.objects.all() 
    return render(request, 'baby_list.html', {'babies': babies})

@login_required
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

@login_required
def baby_page(request):
    return render(request, 'baby.html')

@login_required
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

@login_required
def arrival_list(request):
    arrivals = Arrivalform.objects.all()
    return render(request, 'arrival_list.html',{'arrivals':arrivals})

@login_required
def depature_list(request):
    depatures = Depatureform.objects.all()
    return render(request, 'depature_list.html',{'depatures':depatures})

@login_required
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

@login_required
def payment_list(request):
    payment = Paymentform.objects.all()
    return render(request, 'payment_list.html',{'payment':payment})
@login_required
def payment_page(request):
    return render(request, 'payment.html')

@login_required
def payform(request):
    if request.method == 'POST':
        form=AddPayform(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('sitters_payment_list')
    else:
        form = AddPayform()
    return render(request, 'pay.html',{'form':form})

@login_required
def sitters_payment_list(request):
    s_payment_list = Payform.objects.all()
    return render(request,'s_payment_list.html',{'s_payment_list':s_payment_list})

@login_required
def dollshop(request):
    if request.method == 'POST':
        form = AddShop(request.POST)
        if form.is_valid():
            form.save()
        return redirect('shop_list') 
    else:
        form = AddShop()
    return render(request, 'shop.html', {'form': form})

@login_required
def shop_list(request):
    shop = Shopform.objects.all()
    return render(request,'shop_list.html',{'shop':shop})

@login_required
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

@login_required
def pro_list(request):
    pro = Proform.objects.all()
    return render(request,'pro_list.html',{'pro':pro})



@login_required
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

def dollsell(request, pk):
    # Fetch the Sellingform object with the provided pk, or return a 404 error if not found
    doll = get_object_or_404(Sellingform, pk=pk)
    
    if request.method == 'POST':
        # If the request method is POST, create a form instance with the POST data and the fetched doll object
        form = AddSellingform(request.POST, instance=doll)
        if form.is_valid():
            # If the form is valid, save it to the database
            form.save()
            # Redirect to a success page or another appropriate URL
            return redirect('selldoll_list')  # Replace 'success_url_name' with the actual URL name
    else:
        # If the request method is not POST, create a new form instance without any initial data
        form = AddSellingform()
    
    # Render the 'sell_doll.html' template with the form object
    return render(request, 'sell_doll.html', {'form': form})

def dollsell_without_pk(request):
    # Assuming you want to render a template when accessing sell_doll without a pk
    return render(request, 'sell_doll.html')
@login_required
def proo(request):
    if request.method == 'POST':
        form=AddSellingform(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('selldoll_list')
    else:
        form = AddSellingform()
        return render(request, 'sell_doll.html',{'form':form})


@login_required
def dollsell_list(request):
    selldoll = Sellingform.objects.all()
    return render(request, 'selldoll_list.html', {'selldoll': selldoll})