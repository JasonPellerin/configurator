from django.shortcuts import render 
from django.shortcuts import render_to_response 
from django.template import RequestContext 
from product.models import Product, Category 
#from django.contrib.auth.models import User
# Create your views here.
def ProductsAll(request):
 	products = Product.objects.all().order_by('part_number')
	context = {'products': products } 
	return render_to_response('productsall.html', context, context_instance=RequestContext(request)) 

def CategorysAll(request): 
	categorys = Category.objects.all().order_by('name') 
	context = {'categorys': categorys } 
	return render_to_response('categorysall.html', context, context_instance=RequestContext(request)) 

def SpecificProduct(request, productslug): 
	product = Product.objects.get(slug=productslug) 
	context = { 'product': product } 
	return render_to_response('singleproduct.html', context, context_instance=RequestContext(request)) 

def SpecificCategory(request, categoryslug): 
	category = Category.objects.get(slug=categoryslug) 
	products = Product.objects.filter(category=category) 
	context = {'products': products} 
	return render_to_response('singlecategory.html', context, context_instance=RequestContext(request))
