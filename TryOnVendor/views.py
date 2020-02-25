from django.shortcuts import render
from django.views import View
from TryOn import form as forms


class VendorView(View):  # Vendor Registration
    def get(self, request):
        # form = forms.VendorForm(request.POST or None)
        # context = {'form': form, 'form_id': 'user_register', 'title': 'Vendor Registration'}
        context = {'title': 'Vendor'}
        return render(request, 'base.html', context)

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