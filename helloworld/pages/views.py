from django import forms
from django.views import View
from django.shortcuts import render, redirect
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
    
class Product:
    products = [
        {'id': 1, 'name': 'Product 1', 'description': 'This is the product 1'},
        {'id': 2, 'name': 'Product 2', 'description': 'This is the product 2'},
        {'id': 3, 'name': 'Product 3', 'description': 'This is the product 3'},
        {'id': 4, 'name': 'Product 4', 'description': 'This is the product 4'},
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
        product = Product.products[int(id) - 1]
        viewData['title'] = product['name'] + ' - Online Store'
        viewData['subtitle'] = product['name'] + '- Product detail'
        viewData['product'] = product

        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

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
            return redirect(form)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
    
