from django import forms
from basicform_app.models import User

class Formname(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Your Email Again !")
    text = forms.CharField(widget=forms.Textarea)
    


    def clean(self):
        all_clean_data = super().clean() # data cleaner
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email didn't match !")

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'