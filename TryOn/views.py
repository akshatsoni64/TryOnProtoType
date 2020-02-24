from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from TryOn import form as forms
from TryOn.models import *
from TryOn import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User,auth

@csrf_exempt
def index(request):  
    data=request.GET.get('name')
    print(data)
    result=[]
    #alldata=Product.objects.all()
    imagedata=ProductImages.objects.all()
    if request.method == "POST":
        if request.POST.get('name'):
            prid=request.POST.get('name')
            print("-----",prid)
            pdetails=ProductImages.objects.get(id=prid)
            return render(request,'product-details.html',{'pdetails':pdetails})
        
    return render(request,'index.html',{'data':imagedata})
   
def shop(request):
    return render(request,'shoping-cart.html')

def features(request):
    return render(request,'product.html')

def contact(request):
    return render(request,'contact.html')

def product_details(request):
    return render(request,'product-detail.html')


class LoginView(View):
    def auth(self, uid, pwd, modelName):
        if modelName == 'customer':
            modl = models.Customer
        elif modelName == 'vendor':
            modl = models.Vendor
        elif modelName == 'shipper':
            modl = models.Shipper
        cred = modl.objects.get(username=uid)
        print("Credentials: ", cred.username, cred.password, pwd)
        if cred:
            return True if cred.password == pwd else False
        else:
            return False

    def get(self, request):
        form = forms.LoginForm(request.POST or None)
        context = {'form': form, 'form_id': 'login', 'title': 'Login'}
        return render(request, 'index.html', context)

    def post(self, request):
        print(request.POST)
        form = forms.LoginForm(request.POST)
        status = self.auth(uid=request.POST['username'], pwd=request.POST['password'], modelName=request.POST['utype'])
        print("Status: ", status)
        if status:
            request.session['username'] = request.POST['username']
            request.session['password'] = request.POST['password']
            print(request.session)
            return HttpResponse("/vendor/addproducts/") if request.POST['utype'] == "vendor" else HttpResponse("/login/")
        else:
            return HttpResponse("/login/")

    def put(self, request):
        pass

    def delete(self, request):
        pass


class VendorView(View):  # Vendor Registration
    def get(self, request):
        form = forms.VendorForm(request.POST or None)
        context = {'form': form, 'form_id': 'user_register', 'title': 'Vendor Registration'}
        return render(request, 'index.html', context)

    def post(self, request):
        # print(request.POST)
        form = forms.VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Form", form.errors)

        context = {'form': form, 'form_id': 'vendor_register', 'title': 'Vendor Registration'}
        return render(request, 'index.html', context)
        # return True

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ShipperView(View):  # Shipper Registration
    def get(self, request):
        form = forms.ShipperForm(request.POST or None)
        context = {'form': form, 'form_id': 'shipper_register', 'title': 'Shipper Registration'}
        return render(request, 'index.html', context)

    def post(self, request):
        # print(request.POST)
        form = forms.ShipperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Form", form.errors)

        context = {'form': form, 'form_id': 'shipper_register', 'title': 'Shipper Registration'}
        return render(request, 'index.html', context)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CustomerView(View):
    def get(self, request):
        form = forms.CustomerForm(request.POST or None)
        context = {'form': form, 'form_id': 'customer_register', 'title': 'Customer Registration'}
        return render(request, 'index.html', context)

    def post(self, request):
        form = forms.CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error Form")

        context = {'form': form, 'form_id': 'customer_register', 'title': 'Customer Registration'}
        return render(request, 'index.html', context)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ProductUploadView(View):
    def get(self, request):
        form = forms.ProductUploadForm(request.POST or None)
        context = {'form': form, 'title': "Upload Products"}
        return render(request, 'product_upload.html', context)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ProductDisplayView(View):
    def get(self, request):
        # form =
        context = {'title': "Product Display"}
        return render(request, 'product_display.html', context)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
    
 def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
        email = request.POST['email']

        if password1==password2:
            if  User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')    
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            print('password not matching.....')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
 #           request.sessions['is_logged']= True
            return redirect("/")

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:    
        return render(request,'login.html')        
def logout(request):
      auth.logout(request)
      return redirect('/')   
