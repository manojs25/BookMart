from django import forms
from home.models import User
from home import views

class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name','maxlength':'20','style':'width: 378px;','class':'input-field'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Mobile','maxlength':'10','style':'width: 378px;','class':'input-field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','maxlength':'20','style':'width: 378px;','class':'input-field'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'DOB','maxlength':'20','style':'width: 378px;','class':'input-field'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':' Address'}))#TextInput(attrs={'maxlength':'20','style':'width: 290px;','placeholder':'Address','class':'input-field'}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','maxlength':'8','style':'width: 378px;','class':'input-field'}))

    class Meta:
        model = User
        fields = '__all__'

    def clean_mobile(self):
        mobileno = self.cleaned_data['mobile']
        if len(str(mobileno)) != 10:
            error1 = "Mobile No should contain 10 digits"
            raise forms.ValidationError(error1)
        return mobileno

    def clean_passwd(self):
        passw = self.cleaned_data['passwd']
        if len(passw) <= 5:
            error = 'Password length must between 6 to 8'
            raise forms.ValidationError(error)
        return passw


class ProfileForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name','maxlength':'20','style':'width: 378px;','class':'input-field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','maxlength':'20','style':'width: 378px;','class':'input-field'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':' Address'}))#TextInput(attrs={'maxlength':'20','style':'width: 290px;','placeholder':'Address','class':'input-field'}))

class LoginForm(forms.Form):
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'MOBILE NO','maxlength':'10'}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'PASSWORD','maxlength':'8'}))

    def clean(self):
        mobileno = self.cleaned_data['mobile']
        passw = self.cleaned_data['passwd']
        userm = User.objects.filter(mobile=mobileno)
        userp = User.objects.filter(mobile=mobileno,passwd=passw)

        if userm.exists():
            if userp.exists():
                return self.cleaned_data
            else:
                raise forms.ValidationError("Password is Wrong")
        else:
            raise forms.ValidationError("User not exists")

class OrderDeleteForm(forms.Form):
    order_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'ORDER NUMBER','maxlength':'10','class':'input-field'}))
