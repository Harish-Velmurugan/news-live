from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup
def HomePageView(request): 
    template_name = 'users/home.html'
    r1 = requests.get("https://timesofindia.indiatimes.com/city/chennai")
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html5lib')
    coverpage_news = soup1.find_all('ul',class_="top-newslist clearfix")
    lis = []
    for ul in coverpage_news:
        for li in ul.findAll('li'):
            if li.find('ul'):
                break
            lis.append(li.get_text())
    for i in lis:
        if i == '':
            lis.remove(i)
    return render(request,template_name,{'news':lis})
