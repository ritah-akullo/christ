from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from.models import *

class AddDuty(ModelForm):
      class Meta:
            model = OnDutyform
            fields = '__all__'

class AddBaby(ModelForm):
 class Meta:
        model = Babyform
        fields = '__all__'
    
class AddSitter(ModelForm):
        class Meta:
            model = Sittersform
            fields = '__all__'

class AddDepature(ModelForm):
      class Meta:
       model = Depatureform
       fields = '__all__'

class AddArrival(ModelForm):
      class Meta:
       model = Arrivalform
       fields = '__all__'


class AddPayment(ModelForm):
       class Meta:
        model = Paymentform
        fields = '__all__'

class AddPayform(ModelForm):
    class Meta:
        model = Payform
        fields = '__all__'

class AddShop(ModelForm):
    class Meta:
        model = Shopform
        fields = '__all__'


class AddProform(forms.ModelForm):
    class Meta: 
        model = Proform
        fields = '__all__'

class AddSellingform(ModelForm):
    class Meta:
        model = Sellingform
        fields = '__all__'