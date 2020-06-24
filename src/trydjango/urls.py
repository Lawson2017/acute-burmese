
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
	path('', home_view),
	path('contact/', contact_view),
    path('admin/', admin.site.urls),
    path('create/',product_create_view),
    path('product/',product_detail_view),
    path('about/', about_view),

]
