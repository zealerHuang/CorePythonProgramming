"""dj4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views # new
from calc import views as calc_views # calc

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', calc_views.index), # new
    url(r'^add/$', calc_views.add, name='add'), # calc
    url(r'^add2/(\d+)/(\d+)/', calc_views.add2, name='add2'), # add2
    url(r'^home/', learn_views.home, name='home'), # home
    url(r'^index/', calc_views.index, name='calc_index'), # calc_index_get
]
