import requests
from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect

from .models import Feed
from .tasks import populate_db
from django.core.paginator import Paginator
from background_task.models import Task

def pre_task(repeat):

    Task.objects.all().delete()
    populate_db(repeat=repeat)

def index(request):
    # datatable dashboard view
    pre_task(repeat=100)
    all_videos = Feed.objects.all().order_by('-published_at')
    paginator = Paginator(all_videos, 20)
    page = request.GET.get('page')
    videos = paginator.get_page(page)
    return render(request, 'video_search/index.html', {'Videos': videos})


def search(request):
    # youtube search view
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        # for parsing date-time ::  https://pypi.org/project/isodate/         
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos' : videos
    }
    
    return render(request, 'video_search/search.html', context)