from app.forms import EventForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Event, Like
import json
from django.contrib import messages

# Create your views here.
def home(request):
    events = Event.objects.all()

    if request.user.is_authenticated:
        customer = request.user
        likes = Like.objects.filter(customer=customer)

    context = {'events':events}
    return render(request,'app/home.html',context)

def likes(request):
    
    if request.method == 'POST':
        
        eventId = request.POST['id']

        if request.user.is_authenticated:
            customer = request.user
            likes = Like.objects.filter(customer=customer)

            if likes:
                # for like in likes:
                try:
                    likedEvent = Like.objects.get(event_id=eventId)
                    Event.objects.filter(id=eventId).update(is_liked='False')
                    likedEvent.delete()
                    liked = False
                except:
                    likedEvent = Like.objects.create(customer=customer,event_id=eventId)
                    Event.objects.filter(id=eventId).update(is_liked='True')
                    liked=True
            else:
                likedEvent = Like.objects.create(customer=request.user,event_id=eventId)
                Event.objects.filter(id=eventId).update(is_liked='True')
                liked=True

            ctx={"liked":liked,'eventId':eventId,'login':True}
            return HttpResponse(json.dumps(ctx), content_type='application/json')

        else:
            ctx={'login':False}
            return HttpResponse(json.dumps(ctx), content_type='application/json')


    if request.user.is_authenticated:
            customer = request.user
            likedEvt = Like.objects.filter(customer=customer)

            context={'likedEvt':likedEvt}
    else:
        context={}

    return render(request,'app/likes.html',context)

def createEvent(request):
    form = EventForm(request.POST or None , request.FILES)
    if request.method == "POST":
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'app/crtEvt.html',context)