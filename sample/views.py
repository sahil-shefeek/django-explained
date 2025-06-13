from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from django.contrib import messages

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'sample/product_list.html'  # <app_name>/<model_name>_list.html
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'sample/product_detail.html' # <app_name>/<model_name>_detail.html
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'sample/product_form.html' # <app_name>/<model_name>_form.html
    success_url = reverse_lazy('sample:product_list')

    def form_valid(self, form):
        messages.success(self.request, "Product created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error creating the product. Please check the form.")
        return super().form_invalid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'sample/product_form.html' # <app_name>/<model_name>_form.html
    success_url = reverse_lazy('sample:product_list')

    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error updating the product. Please check the form.")
        return super().form_invalid(form)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'sample/product_confirm_delete.html' # <app_name>/<model_name>_confirm_delete.html
    success_url = reverse_lazy('sample:product_list')
    context_object_name = 'product'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Product deleted successfully!")
        return super().delete(request, *args, **kwargs)
