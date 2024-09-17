from lib2to3.fixes.fix_input import context
from pyexpat import model

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def video_page(request: HttpRequest) -> HttpResponse:
    video = model.Video.prefetched.objects.get(id=1)
    context = {'video':video}
    return render(request, 'videos.html', context)
