from django import  forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'price','brand','category','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Title',}),
            'price': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Price',}),
            'brand': forms.Select(attrs={'class': 'form-control','placeholder': 'Brand',}),
            'category': forms.Select(attrs={'class': 'form-control','placeholder': 'Category',}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Description',}),
        }

    # title = forms.CharField(max_length=50,
    #                         widget=forms.TextInput(attrs={'class':'form-control',"placeholder": "Title"}))
    # description = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'class':'form-control',"placeholder": "Description"}))
    # category = forms.CharField(widget=forms.Select(attrs={'class':'form-control',"placeholder": "Category"}))
    # brand = forms.CharField(widget=forms.Select(attrs={'class':'form-control',"placeholder": "Brand"}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',"placeholder": "Price"}))

    # def save(self, commit=True):
    #     product = super().save(commit=True)
    #     if product:
    #         Product.objects.create(
    #             title = product.title,
    #             description = product.description,
    #             select_category = product.select_category,
    #             brand = product.brand,
    #             price = product.price,
    #         )
    #     return product