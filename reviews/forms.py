from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ('rating', )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-primary'
            if field_name == 'rating':
                field.widget.attrs['class'] = 'rating'