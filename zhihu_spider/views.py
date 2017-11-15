# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import urllib2, re
from models import Titles

# Create your views here.
def spider(request):
    url = 'https://www.zhihu.com/topic/19607535/top-answers'
    try:
        urlRequest = urllib2.Request(url)
        urlResponse = urllib2.urlopen(urlRequest)
    except urllib2.URLError:
        return HttpResponse("网络出差错了呢0.0")
    content = urlResponse.read()
    #这里用正则处理知乎上的h2标题，有个大坑0,0知乎居然还换行了...
    pattern = re.compile('<h2><a class="question_link.*?>(.*?)</a></h2>',re.S)
    titles = re.findall(pattern, content)
    if not titles:
        return HttpResponse("没有找到匹配结果呢0.0")
    for t in titles:
        data = Titles(title=t)
        data.save()
    return HttpResponse("储存成功~")