from operator import itemgetter 
import requests
from django.shortcuts import render

# Make an API call and store the response.
def hacker_news_api_selector():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json' 
    r = requests.get(url)
    submission_list = r.json()
    context = {}
    context['objects'] = []

    # Process information about each submission.
    for submission_id in submission_list[:10]:

        # Make a separate API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" 
        r = requests.get(url)
        response_dict = r.json()
        context['objects'].append(response_dict)

    return context 

def home(request):
    context = hacker_news_api_selector()
    return render(request, "news_api/home.html", context)