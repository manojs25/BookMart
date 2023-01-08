from django import forms
from home.models import User
from kannada_books import views

class PaymentForm(forms.Form):
    CHOICES = [
        ('GooglePay', 'GooglePay'),
        ('PhonePe', 'PhonePe'),
        ('Cards', 'Credit/Debit/ATM Card'),
        ('COD', 'Cash on Delivery'),
    ]
    payment = forms.ChoiceField(widget=forms.RadioSelect(), choices = CHOICES)
