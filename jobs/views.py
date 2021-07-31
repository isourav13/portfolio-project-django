from django.shortcuts import render, get_object_or_404

from .models import Job,Resume
from django.http import FileResponse, Http404
import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    jobs = Job.objects
    resumes = Resume.objects
    return render(request, 'jobs/home.html',{'jobs':jobs,'resumes':resumes})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})


# def resume(request):
#     resumes = Resume.objects
#     return render(request, 'jobs/home.html',{'resumes':resumes})


# def resume(request):
#     if request.method == 'POST':
#         resume = Resume(request.POST, request.FILES)
#         if resume.is_valid():
#             # file is saved
#             resume.save()
#             return Resume('/success/url/')
#     else:
#         resume = Resume()
#     return render(request, 'home.html', {'resumes': resume})