from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            "book_name": forms.TextInput(attrs={'class': 'form-control'}),
            "author_name": forms.TextInput(attrs={'class': 'form-control'}),
            "publication": forms.TextInput(attrs={'class': 'form-control'}),
            "book_price": forms.NumberInput(attrs={'class': 'form-control'}),
            "book_quantity": forms.NumberInput(attrs={'class': 'form-control'}),
            "payment_mode": forms.Select(attrs={'class': 'form-control'}),
        }
