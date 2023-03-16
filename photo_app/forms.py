from django import forms
from django.core import validators
from photo_app.models import Photo

# class UploadForm2(forms.Form):
#     title = forms.CharField(max_length=64, required=True)
#     image = forms.ImageField(allow_empty_file=False, required=True)
#     botcatcher = forms.CharField(required=False, 
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxValueValidator(0)])

class UploadForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = ['title', 'image']

class EditForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = ['title']