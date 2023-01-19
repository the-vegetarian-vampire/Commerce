from django import forms

from .models import Listing, Bid

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']
        widgets= {
            'bid': forms.NumberInput(attrs={'class': 'form-control'})
        }