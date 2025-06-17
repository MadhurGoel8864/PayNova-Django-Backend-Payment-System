from django import forms
from core.models import CreditCard

class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Card Holder Name"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Expiry Month"}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Expiry Month"}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"CVV"}))

    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'month', 'year', 'cvv', 'card_type']

class AmountForm(forms.ModelForm):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"₹30"}))
    
    class Meta:
        model = CreditCard
        fields = ['amount']

class DepositForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter amount to deposit'
        })
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter description (optional)'
        })
    )
