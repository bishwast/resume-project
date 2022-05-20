from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
# Function for sunil view paths. This fun will render htmm code to the user using render.
def home(request):
    # Adding Job objects from the django database to the views
    jobs = Job.objects
    # Added list of jobs above to the views to render jobs info
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})
