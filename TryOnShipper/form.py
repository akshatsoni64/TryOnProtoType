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


class ShipperForm(forms.ModelForm):
    sname = forms.CharField(label="Company Name", widget=forms.TextInput(
        attrs={
            'id': "snameShipper",
            'maxlength': '30',
            'placeholder': 'Name Here...'
        }
    ))
    owner_fname = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'id': "fnameShipper",
            'maxlength': '30',
            'placeholder': 'First Name'
        }
    ))
    owner_lname = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'id': "lnameShipper",
            'maxlength': '30',
            'placeholder': 'Last Name'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "usernameShipper",
            'maxlength': '30',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': "passwordShipper",
            'maxlength': '30',
            'placeholder': 'Password'
        }
    ))
    mobile = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "mobShipper",
            'max': '9999999999',
            'placeholder': 'Mobile Number'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'id': "emailShipper",
            'maxlength': '50',
            'placeholder': 'Email Address'
        }
    ))
    business_address = forms.CharField(label="Address", widget=forms.TextInput(
        attrs={
            'id': "bAddShipper",
            'maxlength': '100',
            'placeholder': 'Business Address'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "cityShipper",
            'maxlength': '30',
            'placeholder': 'City'
        }
    ))
    pincode = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "pincodeShipper",
            'max': '999999',
            'placeholder': 'Pincode'
        }
    ))
    state = forms.ChoiceField(label="State", choices=stateChoice)
    zone = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "zoneShipper",
            'maxlength': '30',
            'placeholder': 'Zone'
        }
    ))
    gst_no = forms.CharField(label="GST Number", widget=forms.TextInput(
        attrs={
            'id': "gstShipper",
            'maxlength': '15',
            'placeholder': 'GST Number'
        }
    ))
    aadhar_no = forms.IntegerField(label="Aadhar Number", widget=forms.NumberInput(
        attrs={
            'id': "aadharShipper",
            'max': '999999999999',
            'placeholder': 'Aadhar Number'
        }
    ))
    tradelicense_id = forms.IntegerField(label="Trade License Number", widget=forms.NumberInput(
        attrs={
            'id': "tradelicenseShipper",
            'max': '99999999999999',
            'placeholder': 'Trade License ID'
        }
    ))
    permit_document = forms.FileField(label="Documents for Permission", widget=forms.ClearableFileInput(
        attrs={
            'id': 's_doc',
            'class': 'DocUpload'
        }
    ))
    address_proof = forms.FileField(label="Address Proof", widget=forms.ClearableFileInput(
        attrs={
            'id': 's_add',
            'class': 'DocUpload'
        }
    ))
    request_status = forms.CharField(widget=forms.HiddenInput(
        attrs={
            'value': 'False'
        }
    ))
    class Meta:
        model = Shipper
        fields = '__all__'
