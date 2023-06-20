"""SmoothieDaddi_Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from shop.views import MenuViewSet
from shop.views import UserRegistrationView, UserLoginView, ContactFormView, AddToCartView, DeleteCartItemView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.views.static import serve

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet , basename='products')

urlpatterns = [
    path('api/', include(router.urls)),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/delete/<int:pk>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('api/contact/', ContactFormView.as_view(), name='contact_form'),

] 

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
