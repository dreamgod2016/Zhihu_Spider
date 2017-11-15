from django.conf.urls import url
from django.contrib import admin
import zhihu_spider.views

urlpatterns = [
    url(r'^$', zhihu_spider.views.spider),
]
