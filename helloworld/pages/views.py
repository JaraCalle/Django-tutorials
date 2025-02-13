from django import forms
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page...",
            "author": "Developed by: Juan José Jara",
        })

        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "email": "Jaracalle2041@gmail.com",
            "address": "Calle 51 #02-02",
            "phone_number": "+573223334444.",
        })

        return context
    
class Product:
    products = [
        {'id': 1, 'name': 'Product 1', 'description': 'This is the product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'description': 'This is the product 2', 'price': 200},
        {'id': 3, 'name': 'Product 3', 'description': 'This is the product 3', 'price': 300},
        {'id': 4, 'name': 'Product 4', 'description': 'This is the product 4', 'price': 400},
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id) - 1]
        except IndexError:
            return HttpResponseRedirect(reverse('home'))

        viewData['title'] = product['name'] + ' - Online Store'
        viewData['subtitle'] = product['name'] + '- Product detail'
        viewData['product'] = product

        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True, min_value=0)

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData['title'] = 'Create product'
        viewData['form'] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return redirect("created")
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class ProductCreatedView(View):
    template_name = 'products/created.html'

    def get(self, request):
        viewData = {}
        viewData['title'] = 'Product created'
        return render(request, self.template_name, viewData)
