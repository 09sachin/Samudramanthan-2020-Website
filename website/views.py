from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import events, sponsers, team, gallery
from .forms import FeedbackCreate, Register

# Create your views here.

from django.http import HttpResponse
from .admin import eventResource

def export(request):
    event_resource = eventResource()
    dataset = event_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="events.csv"'
    return response


def index(request):
    sponser_all = sponsers.objects.all()
    all_det_count = 0

    if request.method == 'POST':
        print('success1')
        form = FeedbackCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' form submitted successfully')

            return HttpResponseRedirect('/#contact')

        else:
            form = FeedbackCreate(request.POST)
            messages.error(request,'invalid form')
    else:
        form = FeedbackCreate()

    context = {'all_det_count': all_det_count,
               'sponser_all':  sponser_all,
               'form': form}

    return render(request, 'website/index.html', context)


def registerf(request):
    all_details = events.objects.all()

    context = {'all_details': all_details}

    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = Register()


    return render(request, 'website/contact.html', context)


def teamf(request):
    team_details = team.objects.all()

    context = {'team_details': team_details,}

    return render(request, 'website/team.html', context)

def galleryf(request):
    gallery_details = gallery.objects.all()

    context = {'gallery_details': gallery_details, }
    return render(request, 'website/gallery.html', context)

def eventsf(request):
    all_details = events.objects.all()

    context = {'all_details': all_details}
    return render(request, 'website/events.html', context)

def sponsersf(request):
    sponser_all = sponsers.objects.all()
    context = {'sponser_all':  sponser_all}

    return render(request, 'website/sponsers.html', context)




