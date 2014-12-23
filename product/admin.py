from django.contrib import admin 
from product.models import Product, Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields 	= {'slug': ('part_number',)} 
	list_display 		= ('part_number', 'category', 'mount', 'management') 
	search_fields 		= ['part_number'] 



class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields 	= {'slug': ('name',)} 
	search_fields 		= ['name'] 

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
