from django.conf.urls import * 
from django.conf import settings 
from django.views.generic import RedirectView 
from django.contrib import admin 
admin.autodiscover()  
urlpatterns = patterns('',
     url(r'^$', 'views.index', {"template": "index.html"}, name="index"),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {         'document_root': settings.MEDIA_ROOT     }),
     (r'^admin/', include(admin.site.urls)),
     (r'^products/$', 'product.views.ProductsAll'),
     (r'^categorys/$', 'product.views.CategorysAll'),
     (r'^products/(?P<productslug>.*)/$', 'product.views.SpecificProduct'),
     (r'^categorys/(?P<categoryslug>.*)/$', 'product.views.SpecificCategory'),  
     (r'^register/$', 'customer.views.CustomerRegistration'),
     (r'^login/$', 'customer.views.LoginRequest'),
     (r'^logout/$', 'customer.views.LogoutRequest'),
     (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
     (r'^resetpassword/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/reset/done/'}),
     (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
     (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
     (r'^profile/$', 'customer.views.UserProfile'),

)  
admin.site.site_header = 'Cyber Switching Admin'
