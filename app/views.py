from app.forms import EventForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Event, Like
import json

# Create your views here.
def home(request):
    events = Event.objects.all()

    context = {'events':events}
    return render(request,'app/home.html',context)

def likes(request):
    
    if request.method == 'POST':
        
        eventId = request.POST['id']

        if request.user.is_authenticated:
            customer = request.user
            likes = Like.objects.filter(customer=customer)

            if likes:
                for like in likes:
                            try:
                                likedEvent = Like.objects.get(event_id=eventId)
                                likedEvent.delete()
                                liked = False
                            except:
                                likedEvent = Like.objects.create(customer=customer,event_id=eventId)
                                liked=True
            else:
                likedEvent = Like.objects.create(customer=request.user,event_id=eventId)
                liked=True

            ctx={"liked":liked,'eventId':eventId}
            return HttpResponse(json.dumps(ctx), content_type='application/json')

    if request.user.is_authenticated:
            customer = request.user
            likes = Like.objects.filter(customer=customer)


    context={'likes':likes}

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