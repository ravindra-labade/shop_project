from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"

        widgets = {
            "shop_name": forms.TextInput(attrs={'class': 'form-control'}),
            "shop_address": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            "shop_owner": forms.TextInput(attrs={'class': 'form-control'}),
            "operated_since": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "available_services": forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            "payment_mode": forms.Select(attrs={'class': 'form-control'}),
        }
