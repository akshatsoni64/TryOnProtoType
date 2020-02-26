from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from TryOn import form as forms
from TryOn.models import *
from TryOnVendor.models import *
from TryOnShipper.models import *
from TryOn.form import *
from TryOnVendor.form import *
from TryOnShipper.form import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User, auth


class RegisterView(View):
    def get(self, request):
        form = CustomerRegisterForm(request.POST)
        context = {'form': form}
        return render(request, 'register.html', context)

    def post(self, request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            template = 'index.html'
        else:
            print("Error Form", form.errors)
            template = 'register.html'

        # context = {'form': form, 'form_id': 'customer_register', 'title': 'Customer Registration'}
        context = {'form': form, 'error': form.errors}
        return render(request, template, context)


@csrf_exempt
def index(request):
    data = request.GET.get('name')
    print(data)
    result = []
    # alldata=Product.objects.all()
    imagedata = ProductImages.objects.all()
    if request.method == "POST":
        if request.POST.get('name'):
            prid = request.POST.get('name')
            print("-----", prid)
            pdetails = ProductImages.objects.get(id=prid)
            return render(request, 'product-detail.html', {'pdetails': pdetails})

    return render(request, 'index.html', {'data': imagedata})


def shop(request):
    return render(request, 'shoping-cart.html')


def features(request):
    return render(request, 'product.html')


def contact(request):
    return render(request, 'contact.html')


def product_details(request):
    return render(request, 'product-detail.html')


"""def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # request.sessions['is_logged']= True
            return redirect("/")

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')"""


def logout(request):
    auth.logout(request)
    return redirect('/')


class LoginView(View):
    def auth(self, uid, pwd):
        cred = Customer.objects.get(username=uid)
        print("Credentials: ", cred.username, cred.password, pwd)
        if cred:
            return True if cred.password == pwd else False
        else:
            return False

    def get(self, request):
        form = LoginForm(request.POST or None)
        context = {'form': form, 'form_id': 'login', 'title': 'Login'}
        return render(request, 'login.html', context)

    def post(self, request):
        print(request.POST)
        form = LoginForm(request.POST)
        status = self.auth(uid=request.POST['username'], pwd=request.POST['password'])
        print("Status: ", status)
        cust_name = Customer.objects.get(username=request.POST['username'])
        context = {'form': form, 'cust_name': cust_name.f_name}
        if status:
            request.session['username'] = request.POST['username']
            request.session['password'] = request.POST['password']
            print(request.session)
            return render(request, 'index.html', context)
        else:
            return render(request, 'login.html', context)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CustomerView(View):
    def get(self, request):
        pass

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
