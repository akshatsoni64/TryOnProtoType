from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from TryOn import form as cforms
from TryOnVendor import form as vforms
from TryOnShipper import form as sforms
from TryOn.models import *
from TryOnVendor.models import *
from TryOnShipper.models import *


class ShipperView(View):  # Shipper Registration
    def get(self, request):
        # form = cforms.ShipperForm(request.POST or None)
        # context = {'form': form, 'form_id': 'shipper_register', 'title': 'Shipper Registration'}
        context = {'title': 'Shipper'}
        return render(request, 'shipper.html', context)

    def post(self, request):
        # print(request.POST)
        pass
        """form = cforms.ShipperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Form", form.errors)

        context = {'form': form, 'form_id': 'shipper_register', 'title': 'Shipper Registration'}
        return render(request, 'index.html', context)"""

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ShipperLogin(View):
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
        return render(request, 'shipper_login.html', context)

    def post(self, request):
        pass
        """print(request.POST)
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
            return HttpResponse("/login/")"""

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ShipperRegister(View):
    def get(self, request):
        form = sforms.ShipperForm(request.POST or None)
        context = {'form': form, 'form_id': 'user_register', 'title': 'Shipper Registration'}
        # context = {'title': 'Vendor'}
        return render(request, 'shipper_registration.html', context)

    def post(self, request):
        # print(request.POST)
        form = sforms.ShipperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("Error Form", form.errors)

        context = {'form': form, 'form_id': 'vendor_register', 'title': 'Vendor Registration'}
        return render(request, 'shipper_registration.html', context)
