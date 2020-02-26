from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from TryOn import form as cforms
from TryOn.models import *
from TryOnVendor.models import *
from TryOnShipper.models import *


class VendorView(View):  # Vendor Registration
    def get(self, request):
        # form = cforms.VendorForm(request.POST or None)
        # context = {'form': form, 'form_id': 'user_register', 'title': 'Vendor Registration'}
        context = {'title': 'Vendor'}
        return render(request, 'vendor.html', context)

    def post(self, request):
        # print(request.POST)
        pass
        """form = cforms.VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Form", form.errors)

        context = {'form': form, 'form_id': 'vendor_register', 'title': 'Vendor Registration'}
        return render(request, 'index.html', context)"""
        # return True

    def put(self, request):
        pass

    def delete(self, request):
        pass


class VendorLogin(View):
    def auth(self, uid, pwd, modelName):
        if modelName == 'customer':
            modl = Customer
        elif modelName == 'vendor':
            modl = Vendor
        elif modelName == 'shipper':
            modl = Shipper
        cred = modl.objects.get(username=uid)
        print("Credentials: ", cred.username, cred.password, pwd)
        if cred:
            return True if cred.password == pwd else False
        else:
            return False

    def get(self, request):
        form = cforms.LoginForm(request.POST or None)
        context = {'form': form, 'form_id': 'login', 'title': 'Login'}
        return render(request, 'vendor_login.html', context)

    def post(self, request):
        print(request.POST)
        form = cforms.LoginForm(request.POST)
        status = self.auth(uid=request.POST['username'], pwd=request.POST['password'], modelName=request.POST['utype'])
        print("Status: ", status)
        if status:
            request.session['username'] = request.POST['username']
            request.session['password'] = request.POST['password']
            print(request.session)
            return HttpResponse("/vendor/addproducts/") if request.POST['utype'] == "vendor" else HttpResponse(
                "/login/")
        else:
            return HttpResponse("/login/")

    def put(self, request):
        pass

    def delete(self, request):
        pass


class VendorRegister(View):
    def get(self, request):
        form = cforms.VendorForm(request.POST or None)
        context = {'form': form, 'form_id': 'user_register', 'title': 'Vendor Registration'}
        # context = {'title': 'Vendor'}
        return render(request, 'vendor_registration.html', context)

    def post(self, request):
        # print(request.POST)
        form = cforms.VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Form", form.errors)

        context = {'form': form, 'form_id': 'vendor_register', 'title': 'Vendor Registration'}
        return render(request, 'vendor_registration.html', context)


class ProductUploadView(View):
    def get(self, request):
        form = cforms.ProductUploadForm(request.POST or None)
        context = {'form': form, 'title': "Upload Products"}
        return render(request, 'product_upload.html', context)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
