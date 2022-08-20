from django import forms
from .models import Discount


class DiscountForm(forms.ModelForm):
    """
    Form for addming a new discount in the system
    """
    class Meta:
        model = Discount
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'


class ApplyDiscountForm(forms.ModelForm):
    """
    Form to check if code exists in database
    """
    class Meta:
        model = Discount
        fields = ('code', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'
            field.label = False
