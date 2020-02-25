from django.shortcuts import render
from django.views import View

from TryOn import form as forms


class ShipperView(View):  # Shipper Registration
    def get(self, request):
        # form = forms.ShipperForm(request.POST or None)
        # context = {'form': form, 'form_id': 'shipper_register', 'title': 'Shipper Registration'}
        context = {'title': 'Shipper'}
        return render(request, 'base.html', context)

    def post(self, request):
        # print(request.POST)
        pass
        """form = forms.ShipperForm(request.POST, request.FILES)
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
