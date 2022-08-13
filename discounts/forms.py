from django import forms
from .models import Discount


class DiscountForm(forms.ModelForm):

    class Meta:
        model = Discount
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'


class ApplyDiscountForm(forms.ModelForm):
    """
    sss
    """
    class Meta:
        model = Discount
        fields = ('code', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'
            field.label = False