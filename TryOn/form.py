from django import forms
from TryOn.models import *
from TryOnShipper.models import *
from TryOnVendor.models import *

usersChoice = (
    ("customer", "Customer"),
    ("vendor", "Vendor"),
    ("shipper", "Shipper")
)
stateChoice = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Assam", "Assam"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Orissa", "Orissa"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttrakhand", "Uttrakhand"),
    ("West Bengal", "West Bengal"),
)


class LoginForm(forms.Form):
    # utype = forms.CharField(widget=forms.RadioSelect(choices=usersChoice), label="Type")
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': "username_login",
                'maxlength': '30',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': "password_login",
                'maxlength': '30',
                'placeholder': 'Password'
            }
        )
    )


class CustomerRegisterForm(forms.ModelForm):
    f_name = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'id': "firstname",
            'maxlength': '30',
            'class':'form-input',
            'placeholder': 'First Name'
        }
    ))
    m_name = forms.CharField(label="Middle Name(Optional)", widget=forms.TextInput(
        attrs={
            'id': "middlename",
            'maxlength': '30',
            'class':'form-input',
            'placeholder': 'Middle Name'
        }
    ))
    l_name = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'id': "lastname",
            'maxlength': '30',
            'class':'form-input',
            'placeholder': 'Last Name'
        }
    ))
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            'id': "username",
            'maxlength': '30',
            'class':'form-input',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'id': "password",
            'maxlength': '30',
            'class':'form-input',
            'placeholder': 'Password'
        }
    ))
    mobile = forms.IntegerField(label="Mobile Number", widget=forms.NumberInput(
        attrs={
            'id': "mobileno",
            'max': '9999999999',
            'class':'form-input',
            'placeholder': 'Mobile Number'
        }
    ))
    email = forms.CharField(label="Email ID", widget=forms.EmailInput(
        attrs={
            'id': "email",
            'maxlength': '50',
            'class': 'form-input',
            'placeholder': 'email@address.com'
        }
    ))
    referral = forms.CharField(label="Referral Code", widget=forms.TextInput(
        attrs={
            'id': "referral",
            'maxlength': '20',
            'class': 'form-input',
            'placeholder': 'Referral Code'
        }
    ))
    address = forms.CharField(label="Address", widget=forms.TextInput(
        attrs={
            'id': "address",
            'maxlength': '100',
            'class': 'form-input',
            'placeholder': 'Address'
        }
    ))
    state = forms.ChoiceField(label="State", choices=stateChoice, widget=forms.Select(
        attrs={
            'id': "state",
            'class': 'form-input'
        }
    ))
    city = forms.CharField(label="City", widget=forms.TextInput(
        attrs={
            'id': "city",
            'maxlength': '30',
            'class':'form-input',
            'placeholder': 'City'
        }
    ))
    pincode = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "pincode",
            'maxlength': '30',
            'class': 'form-input',
            'placeholder': 'Pincode'
        }
    ))

    class Meta:
        model = Customer
        fields = '__all__'
