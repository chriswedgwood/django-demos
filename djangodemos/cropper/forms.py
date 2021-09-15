from django import forms

class UploadPhotoForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()