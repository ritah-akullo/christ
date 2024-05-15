from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class CategoryStay(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  



class Sittersform(models.Model):
    c_stay = models.ForeignKey(CategoryStay,on_delete = models.CASCADE,null=True)
    sitter_name = models.CharField(max_length=200,null=True)
    age = models.IntegerField( default = 0)
    telephone_no = models.CharField(max_length=50,null=True )
    gender = models.CharField( max_length=100, null=True)
    religion = models.CharField( max_length=100, null = True,blank = True )
    location = models.CharField(max_length=50, null =True)
    next_of_kin = models.CharField(max_length=200,null=True)
    level_of_education = models.CharField(max_length=50 ,null=True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    
    def _str_(self):
        return self.c_name


class Arrivalform(models.Model):
    b_name = models.CharField(max_length=50,null=True)
    parent_name = models.CharField(max_length=50,null=True)
    timeInDay =  models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    brought_by = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.b_name

class OnDutyform(models.Model):
    name = models.CharField(max_length=50,null=True)
    period = models.DateTimeField(auto_now_add=True)
    baby_assigned_to = models.ForeignKey(Arrivalform, on_delete=models.SET_NULL, null=True,)
    telephone_no = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.name
    

   
class Paymentform(models.Model):
    b_name = models.CharField(max_length=50,null=True)
    amount = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, default='Ugx',null=True,)
    paid_by=  models.CharField(max_length=10,null=True,)
    date = models.DateField(default=timezone.now)
    def __int__(self):
        return self.currency
    
class Sitter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username

class Payform(models.Model):
    s_name= models.CharField(max_length=50,null=True)
    amount = models.IntegerField(default=3000,)
    currency = models.CharField(max_length=10, default='Ugx')
    date= models.DateField(default=timezone.now)
    baby_count = models.IntegerField(null=True, )
    total_amount = models.IntegerField(null=True,)
   
    def total_amount(self):
        total= self.amount * self.baby_count
        return int(total)

    def __int__(self):
        return self.sitter_name
    
class Babyform(models.Model):
    c_stay = models.ForeignKey(CategoryStay,on_delete=models.CASCADE, null=True)
    b_name = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=50,null=True) 
    sponsorname = models.CharField(max_length=100,null=True)
    timeInDay = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.b_name
    


    



class Depatureform(models.Model):
    b_name = models.CharField(max_length=50,null=True)
    parent_name = models.CharField(max_length=50,null=True)
    timeOutDay = models.DateTimeField(default=timezone.now) 
    date = models.DateField(default=timezone.now)
    person_pickingup = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f'Departureform {self.b_name}'
                


                
class Shopform(models.Model):
    doll_name = models.CharField(max_length=50,null=True)
    quality = models.CharField(max_length=50,null=True)
    brand = models.CharField(max_length=50,null=True)
    buying_price = models.CharField(max_length=50,null=True)
    selling_price = models.CharField(max_length=50,null=True)
    total_price = models.CharField(max_length=50,null=True)
    order_date = models.DateField(null=True,default=timezone.now)

    def total(self):
        total= self.buying_price * self.quantity
        return int(total)
    
    def __str__(self):
        return self.doll_name



    

class Proform(models.Model):
        item_name = models.CharField(max_length=50,null=True)
        amount = models.CharField(max_length=50,null=True)
        quantity = models.DecimalField(max_digits=10, decimal_places=0,)
        unit = models.CharField(max_length=10,null=True)
        total_price = models.CharField(max_length=50,null=True)
        order_date = models.DateField(auto_now_add=True)
        

        def __str__(self):
            return self.item_name

class Sellingform(models.Model):
    doll = models.ForeignKey(Shopform, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_date = models.DateField(auto_now_add=True)
    issued_to = models.ForeignKey(Babyform, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True,)
    unit_price = models.IntegerField(default=0, null=True,)
    sold_quantity = models.IntegerField(default=0, null=True,)
    
    def gettotal_amount(self):
      total=self.quantity*self.unit_price
      return int(total)