"""
URL configuration for superpet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from.import views
#. means same package

# ==============import url from product application================
from products import urls
#adding urls.py from products application

#===================static Import=====================
from django.conf.urls.static import static
# ==================import settings=================
from . import settings

# =====================import url from cart application=================
from cart import urls


#. means same package
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/',views.user_login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.user_logout,name="logout"),
    path('products/',include('products.urls')),
    path('cart/',include('cart.urls')),
    path('admin-portal/',views.admin,name="admin-portal"),
    path('profile/',views.profile,name="profile"),
    path('change-password/',views.changePassword,name="change-password")

]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

