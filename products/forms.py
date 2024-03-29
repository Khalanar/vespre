from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form used to create new products
    """
    class Meta:
        """
        Set basic properties
        """
        model = Product
        fields = '__all__'
        exclude = ('rating', )

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Overwrite init method
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'
