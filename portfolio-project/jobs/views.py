from django.shortcuts import render

# Create your views here.
# Function for sunil view paths. This fun will render htmm code to the user using render.
def sunil(request):
    return render(request, 'jobs/sunil.html')