from django.shortcuts import render
from django.template.defaulttags import register
# Create your views here.
from django.views.generic import TemplateView
import requests
import json,urllib.request
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
    response = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=c702ecefa36b48aab22f23445f289bb4")
    jsonResponse = json.load(response)
    
    for i in range(len(jsonResponse['articles'])):
        
        jsonResponse['articles'][i]['publishedAt'] = jsonResponse['articles'][i]['publishedAt'].replace('T'," ").replace("Z","")
        if jsonResponse['articles'][i]['description'] == None :
            jsonResponse['articles'][i]['description'] = "Ooopsssiee!......Description not available" 
    return render(request,template_name,{'news':lis,'articles':jsonResponse['articles']})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
