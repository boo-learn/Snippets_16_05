"""Snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/delete/<int:id>', views.snippet_delete, name="snippet-delete"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippet/<int:id>', views.snippet_detail, name="snippet-detail"),
    path('comment/add', views.comment_add, name="comment-add"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout, name="logout"),
    path('registration', views.register, name="registration"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

