from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from urlparse import urlparse
from string import find
import tweepy

# Create your views here.

def home(request):
   return render(request, 'discover_app/home.html', None)

def whatsnew(request):
   try:
      search_query = request.POST["whats_new_with"]
   except (KeyError):
      return render(request, 'discover_app/home.html',None)

   auth = tweepy.OAuthHandler('DXFRgenSeZg7VXEaxSNg',
                              'HWXErBcS4FeGDyqNV57DxzNJitlTM6pEbeGigO7gg5c')
   auth.set_access_token('529426461-woHMiSSPNWlby6YbDQNcC9baWzmopRpKcmET8rQo',
                         'z38BaRCgMhnOiW46mXj3rneeWePSASrimhw4HK9Utg20x')
   api = tweepy.API(auth)
   res = []
   i = 1

   for tweet in tweepy.Cursor(api.search,q=search_query).items(100):
     if 'http://' in tweet.text:
        middleIndex = find(tweet.text,'http://') - 1
        res2 = "@" + tweet.user.screen_name + ": " + tweet.text[0:middleIndex]
        url = urlparse(tweet.text[find(tweet.text,'http://'):])
        url = url.scheme + '://' +  url.netloc + url.path
        res3 = tweet.text[middleIndex + 1 + len(url):]
        res.append([res2,url,res3])
        i += 1
     if i == 20:
        break

   return render(request, 'discover_app/whatsnew.html', {"res":res,})


