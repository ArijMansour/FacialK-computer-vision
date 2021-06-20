"""django_ML_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import train
from django_ML_API.views import home, about,align,hello

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api2/', include('api.urls')),
    path('api', include(("train.urls", "train"), namespace="train")),
    path('', hello),
    path('about/', about),
    path('align/', align),
    path(r"", include(("file.urls", "file"), namespace="file")),
    path(r"", include(("train.urls", "train"), namespace="train"))

]
