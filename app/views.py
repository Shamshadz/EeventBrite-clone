from multiprocessing import Event
from django.shortcuts import render
from app.models import Event, Like

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
                    for event in event:
                        try:
                            likedEvent = Like.objects.get(event_id=eventId)
                        except:
                            likedEvent = Like.objects.create(customer=customer,event_id=eventId)
            else:
                likes= Like.objects.create(customer=request.user)
                
                likedEvent = Like.objects.create(customer=customer,event_id=eventId)

    if request.user.is_authenticated:
            customer = request.user
            likes = Like.objects.filter(customer=customer)

            for like in likes:
                print(like)
                print(like.event.event_name)


    context={'likes':likes}

    return render(request,'app/likes.html',context)
