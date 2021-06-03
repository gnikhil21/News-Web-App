from django.shortcuts import render,redirect
from newsapi import NewsApiClient
from django.http import HttpResponse
from news import settings

# Create your views here.
def home(request):
    newsapi=NewsApiClient(api_key=settings.APIKEY)
    search = request.GET.get('search', None)
    headlines=newsapi.get_top_headlines(q=search)

    data=headlines["articles"]
    
    page={"data":[],"search":search}

    for i in data:
        page["data"].append({
            "title": i["title"],
            "des"  : i["description"],
            "img"  : i["urlToImage"],
            "url"  : i["url"]
        })

    return render(request,'index.html',page)
