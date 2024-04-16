from django import forms
from django.core.validators import MinValueValidator
from .models import Product, Category, Review, Favorite
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    '''
    Form for adding products
    '''
    
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
        
        
    price = forms.DecimalField(
        validators=[MinValueValidator(0)],
        label='Price',
        widget=forms.NumberInput(attrs={'class': 'border-black rounded-0', 'min': '0', 'step': '0.01'})
    )
    has_sizes = forms.BooleanField(
        label='Has Flavour',
        widget=forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        required=False
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
            

class ReviewForm(forms.ModelForm):
    
    '''
    Form for adding reviews
    '''
    class Meta:
        model = Review
        fields = ['subject', 'rating', 'review']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'subject': 'Subject',
            'rating': 'Rating (1-5)',
            'review': 'Review',
        }
        
        
class FavoriteForm(forms.ModelForm):
    """
    Form for managing user's favorite products.
    """
    class Meta:
        model = Favorite
        fields = ['product']