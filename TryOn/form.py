from django import forms
from . import models

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
    utype = forms.CharField(widget=forms.RadioSelect(choices=usersChoice), label="Type")
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


class VendorForm(forms.ModelForm):
    name = forms.CharField(label="Company Name", widget=forms.TextInput(
        attrs={
            'id': "cnameVendor",
            'maxlength': '30',
            'placeholder': 'Name Here...'
        }
    ))
    owner_fname = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'id': "fnameVendor",
            'maxlength': '30',
            'placeholder': 'First Name'
        }
    ))
    owner_lname = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'id': "lnameVendor",
            'maxlength': '30',
            'placeholder': 'Last Name'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "usernameVendor",
            'maxlength': '30',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'id': "passwordVendor",
            'maxlength': '30',
            'placeholder': 'Password'
        }
    ))
    mobile = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "mobVendor",
            'max': '9999999999',
            'placeholder': 'Mobile Number'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'id': "emailVendor",
            'maxlength': '50',
            'placeholder': 'Email Address'
        }
    ))
    business_address = forms.CharField(label="Address", widget=forms.TextInput(
        attrs={
            'id': "bAddVendor",
            'maxlength': '100',
            'placeholder': 'Business Address'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "cityVendor",
            'maxlength': '30',
            'placeholder': 'City'
        }
    ))
    pincode = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "pincodeVendor",
            'max': '999999',
            'placeholder': 'Pincode'
        }
    ))
    state = forms.ChoiceField(label="State", choices=stateChoice)
    zone = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': "zoneVendor",
            'maxlength': '30',
            'placeholder': 'Zone'
        }
    ))
    gst_no = forms.CharField(label="GST Number", widget=forms.TextInput(
        attrs={
            'id': "gstVendor",
            'maxlength': '15',
            'placeholder': 'GST Number'
        }
    ))
    aadhar_no = forms.IntegerField(label="Aadhar Number", widget=forms.NumberInput(
        attrs={
            'id': "aadharVendor",
            'max': '999999999999',
            'placeholder': 'Aadhar Number'
        }
    ))
    tradelicense_id = forms.IntegerField(label="Trade License Number", widget=forms.NumberInput(
        attrs={
            'id': "tradelicenseVendor",
            'max': '99999999999999',
            'placeholder': 'Trade License ID'
        }
    ))
    permit_document = forms.FileField(label="Documents for Permission", widget=forms.ClearableFileInput(
        attrs={
            'id': 'v_doc',
            'class': 'DocUpload'
        }
    ))
    address_proof = forms.FileField(label="Address Proof", widget=forms.ClearableFileInput(
        attrs={
            'id': 'v_add',
            'class': 'DocUpload'
        }
    ))
    request_status = forms.CharField(widget=forms.HiddenInput(
        attrs={
            'value': 'False'
        }
    ))


    class Meta:
        model = models.Vendor
        fields = '__all__'

    """def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required': ''.format(
                fieldname=field.label)}"""


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
        model = models.Shipper
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    f_name = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'id': "firstname",
            'maxlength': '30',
            'placeholder': 'First Name'
        }
    ))
    m_name = forms.CharField(label="Middle Name(Optional)", widget=forms.TextInput(
        attrs={
            'id': "middlename",
            'maxlength': '30',
            'placeholder': 'Middle Name'
        }
    ))
    l_name = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'id': "lastname",
            'maxlength': '30',
            'placeholder': 'Last Name'
        }
    ))
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            'id': "username",
            'maxlength': '30',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'id': "password",
            'maxlength': '30',
            'placeholder': 'Password'
        }
    ))
    mobile = forms.IntegerField(label="Mobile Number", widget=forms.NumberInput(
        attrs={
            'id': "mobileno",
            'max': '9999999999',
            'placeholder': 'Mobile Number'
        }
    ))
    email = forms.CharField(label="Email ID", widget=forms.EmailInput(
        attrs={
            'id': "email",
            'maxlength': '50',
            'placeholder': 'email@address.com'
        }
    ))
    referral = forms.CharField(label="Referral Code", widget=forms.TextInput(
        attrs={
            'id': "referral",
            'maxlength': '20',
            'placeholder': 'Referral Code'
        }
    ))
    address = forms.CharField(label="Address", widget=forms.TextInput(
        attrs={
            'id': "address",
            'maxlength': '100',
            'placeholder': 'Address'
        }
    ))
    state = forms.ChoiceField(label="State", choices=stateChoice)
    city = forms.CharField(label="City", widget=forms.TextInput(
        attrs={
            'id': "city",
            'maxlength': '30',
            'placeholder': 'City'
        }
    ))
    pincode = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'id': "pincode",
            'maxlength': '30',
            'placeholder': 'Pincode'
        }
    ))

    class Meta:
        model = models.Customer
        fields = '__all__'

class ProductUploadForm(forms.ModelForm):
    vendor_id = forms.CharField(widget=forms.HiddenInput())
    brand = forms.CharField(label="Brand", widget=forms.TextInput(
        attrs={
            'maxlength': '30',
            'placeholder': 'Brand'
        }
    ))
    category = forms.CharField(label="Product Category", widget=forms.TextInput(
        attrs={
            'maxlength': '20',
            'placeholder': 'Category'
        }
    ))
    sub_category = forms.CharField(label="Product Category", widget=forms.TextInput(
        attrs={
            'maxlength': '20',
            'placeholder': 'Sub-Category'
        }
    ))
    description = forms.CharField(label="Product Description", widget=forms.TextInput(
        attrs={
            'maxlength': '200',
            'placeholder': 'Description'
        }
    ))
    type = forms.CharField(label="Product Type", widget=forms.TextInput(
        attrs={
            'maxlength': '10',
            'placeholder': 'Type'
        }
    ))
    material = forms.CharField(label="Product Material", widget=forms.TextInput(
        attrs={
            'maxlength': '20',
            'placeholder': 'Material'
        }
    ))
    price = forms.IntegerField(label="Product Price", widget=forms.NumberInput(
        attrs={
            'max': '999999',
            'placeholder': 'Price'
        }
    ))
    class Meta:
        model = models.Product
        fields = '__all__'

