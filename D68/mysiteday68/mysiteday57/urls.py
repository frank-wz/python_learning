"""mysiteday57 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
# from app01.views import login,publisher_list, add_publisher,delete_publisher, edit_publisher
from app01 import views
urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^publisher_list/$',views.publisher_list),   # 展示出版社列表页面
    url(r'^add_publisher/$',views.add_publisher), # 添加出版社
    url(r'^delete_publisher/$',views.delete_publisher), # 添加出版社
    url(r'^edit_publisher/$',views.edit_publisher), # 添加出版社

# day58   -----   ↓   ------
    url(r'^book_list/$',views.book_list),   # 书籍列表
    url(r'^delete_book/$',views.delete_book),   # 书籍列表
    url(r'^add_book/$',views.add_book),   # 书籍列表
    url(r'^edit_book/$',views.edit_book),   # 书籍列表



    url(r'',views.publisher_list) # 上面所有的都没匹配上，默认就执行publisher_list
]
