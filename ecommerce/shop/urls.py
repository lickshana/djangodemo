"""ecommerce URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from django.conf.urls.static import static
from django.conf import settings

app_name='shop'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.categories,name="categories"),
    path('register',views.registration,name="registration"),
    path('login',views.user_login,name="user_login"),
    path('logout',views.user_logout,name="user_logout"),
    path('products/<int:p>',views.products,name="products"),
    path('product_details/<int:p>',views.product_details,name="product_details"),
    path('add_categories', views.add_categories, name="add_categories"),
    path('add_product', views.add_product, name="add_product"),
    path('add_stock/<int:i>', views.add_stock, name="add_stock"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)