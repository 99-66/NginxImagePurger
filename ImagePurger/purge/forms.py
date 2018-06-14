from django import forms
from django.core import validators
from django.core.validators import URLValidator

from .models import PurgeLog


class URLForm(forms.Form):
    url = forms.URLField(validators=[validators.URLValidator], widget=forms.TextInput(attrs = {
        'class': 'form-control',
        'name': 'url',
        'placeholder': 'Image URL를 입력해주세요',
        'style': 'width: 500px'
    }
    ))
    #
    # def clean_url(self):
    #     url = self.cleaned_data.get('url')
    #     val = URLValidator(verify_exsists=False)
    #     return val(url)
