from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class ProductAddCartForm(forms.Form):
    quantity = forms.TypedChoiceField(initial=1, choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Кол-во')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
