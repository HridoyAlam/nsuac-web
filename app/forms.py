from django import forms

class contact_form(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=11, required=True)
    meessage = forms.CharField(widget=forms.Textarea, required=True)