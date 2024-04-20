from django import forms


class PostForms(forms.Form):
    title = forms.CharField(max_length=10)
    text = forms.CharField(widget=forms.Textarea)
    is_enabled = forms.BooleanField()
class Test(forms.Form):
     title = forms.CharField()
     text = forms.CharField(widget=forms.Textarea)
     is_enabled = forms.BooleanField()
     email = forms.EmailField()


