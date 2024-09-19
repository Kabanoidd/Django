from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from . import models


def video_page(request: HttpRequest, video_id) -> HttpResponse:
    video = models.Video.objects.get(id=video_id)
    context = {'video':video}
    return render(request, 'videos/videos.html', context)
