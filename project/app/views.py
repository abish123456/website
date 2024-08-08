from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages
from app.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
def home(request):
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Invalid Username or Password")
    
    Movies=Movie_collections.objects.filter(status=0)
    Stream=Streaming_collections.objects.filter(status=0)
    Events=Event_collections.objects.filter(status=0)
    Sports=Sports_collections.objects.filter(status=0)
    return render(request,"home.html",{'Movies':Movies, 'Streamings':Stream,'Events':Events,'Sports':Sports}) 
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")
def kanyakumari(request):
    return render(request,"place/kanyakumari.html")
def madurai(request):
    return render(request,"place/madurai.html")
def thanjavur(request):
    return render(request,"place/thanjavur.html")
def coimbatore(request):
    return render(request,"place/coimbatore.html")
def tirichy(request):
    return render(request,"place/tirichy.html")
def chennaimovies(request):
    Movies=Chennai_Tamil_movies.objects.filter(status=0)
    Other=Chennai_Other_movies.objects.filter(status=0)
    Other1=Chennai_Other1_movies.objects.filter(status=0)
    Cartoon=Chennai_Cartoon_movies.objects.filter(status=0)
    return render(request,"chennai/chennaimovies.html",{'Movies':Movies,'Other':Other,'Other1':Other1,'Cartoon':Cartoon}) 
def kumarimovies(request):
    return render(request,"kumari/kumarimovies.html") 
def maduraimovies(request):
    return render(request,"madurai/maduraimovies.html")
def thanjavurmovies(request):
    return render(request,"thanjavur/thanjavurmovies.html")   
def coimbatoremovies(request):
    return render(request,"coimbatore/coimbatoremovies.html")   
def tirichymovies(request):
    return render(request,"tirichy/tirichymovies.html")   
def chennaistreaming(request):
    stream1=Streaming1.objects.filter(status=0)
    stream2=Streaming2.objects.filter(status=0)
    stream3=Streaming3.objects.filter(status=0)
    stream4=Streaming4.objects.filter(status=0)
    return render(request,"streaming/chennaistreaming.html",{'stream1':stream1,'stream2':stream2,'stream3':stream3,'stream4':stream4})  
def maduraistreaming(request):
    stream1=Streaming1.objects.filter(status=0)
    stream2=Streaming2.objects.filter(status=0)
    stream3=Streaming3.objects.filter(status=0)
    stream4=Streaming4.objects.filter(status=0)
    return render(request,"streaming/chennaistreaming.html",{'stream1':stream1,'stream2':stream2,'stream3':stream3,'stream4':stream4}) 
    
def kumaristreaming(request):
    stream1=Streaming1.objects.filter(status=0)
    stream2=Streaming2.objects.filter(status=0)
    stream3=Streaming3.objects.filter(status=0)
    stream4=Streaming4.objects.filter(status=0)
    return render(request,"streaming/chennaistreaming.html",{'stream1':stream1,'stream2':stream2,'stream3':stream3,'stream4':stream4})    
def thanjavurstreaming(request):
    stream1=Streaming1.objects.filter(status=0)
    stream2=Streaming2.objects.filter(status=0)
    stream3=Streaming3.objects.filter(status=0)
    stream4=Streaming4.objects.filter(status=0)
    return render(request,"streaming/chennaistreaming.html",{'stream1':stream1,'stream2':stream2,'stream3':stream3,'stream4':stream4})    
def coimbatorestreaming(request):
    stream1=Streaming1.objects.filter(status=0)
    stream2=Streaming2.objects.filter(status=0)
    stream3=Streaming3.objects.filter(status=0)
    stream4=Streaming4.objects.filter(status=0)
    return render(request,"streaming/chennaistreaming.html",{'stream1':stream1,'stream2':stream2,'stream3':stream3,'stream4':stream4})   
def tirichystreaming(request):
    stream1=Streaming1.objects.filter(status=0)
    stream2=Streaming2.objects.filter(status=0)
    stream3=Streaming3.objects.filter(status=0)
    stream4=Streaming4.objects.filter(status=0)
    return render(request,"streaming/chennaistreaming.html",{'stream1':stream1,'stream2':stream2,'stream3':stream3,'stream4':stream4})    
def chennaievents(request):
    event1=Event1.objects.filter(status=0)
    event2=Event2.objects.filter(status=0)
    event3=Event3.objects.filter(status=0)
    event4=Event4.objects.filter(status=0)
    return render(request,"events/chennaievents.html",{'event1':event1,'event2':event2,'event3':event3,'event4':event4})
def maduraievents(request):
    event1=Event1.objects.filter(status=0)
    event2=Event2.objects.filter(status=0)
    event3=Event3.objects.filter(status=0)
    event4=Event4.objects.filter(status=0)
    return render(request,"events/chennaievents.html",{'event1':event1,'event2':event2,'event3':event3,'event4':event4})
def kumarievents(request):
    event1=Event1.objects.filter(status=0)
    event2=Event2.objects.filter(status=0)
    event3=Event3.objects.filter(status=0)
    event4=Event4.objects.filter(status=0)
    return render(request,"events/chennaievents.html",{'event1':event1,'event2':event2,'event3':event3,'event4':event4})
def thanjavurevents(request):
    event1=Event1.objects.filter(status=0)
    event2=Event2.objects.filter(status=0)
    event3=Event3.objects.filter(status=0)
    event4=Event4.objects.filter(status=0)
    return render(request,"events/chennaievents.html",{'event1':event1,'event2':event2,'event3':event3,'event4':event4})
def coimbatoreevents(request):
    event1=Event1.objects.filter(status=0)
    event2=Event2.objects.filter(status=0)
    event3=Event3.objects.filter(status=0)
    event4=Event4.objects.filter(status=0)
    return render(request,"events/chennaievents.html",{'event1':event1,'event2':event2,'event3':event3,'event4':event4})
def tirichyevents(request):
    event1=Event1.objects.filter(status=0)
    event2=Event2.objects.filter(status=0)
    event3=Event3.objects.filter(status=0)
    event4=Event4.objects.filter(status=0)
    return render(request,"events/chennaievents.html",{'event1':event1,'event2':event2,'event3':event3,'event4':event4})
def chennaisports(request):
    sport1=Sport1.objects.filter(status=0)
    sport2=Sport2.objects.filter(status=0)
    sport3=Sport3.objects.filter(status=0)
    sport4=Sport4.objects.filter(status=0)
    return render(request,"sports/chennaisports.html",{'sport1':sport1,'sport2':sport2,'sport3':sport3,'sport4':sport4})
def maduraisports(request):
    sport1=Sport1.objects.filter(status=0)
    sport2=Sport2.objects.filter(status=0)
    sport3=Sport3.objects.filter(status=0)
    sport4=Sport4.objects.filter(status=0)
    return render(request,"sports/chennaisports.html",{'sport1':sport1,'sport2':sport2,'sport3':sport3,'sport4':sport4})
def kumarisports(request):
    sport1=Sport1.objects.filter(status=0)
    sport2=Sport2.objects.filter(status=0)
    sport3=Sport3.objects.filter(status=0)
    sport4=Sport4.objects.filter(status=0)
    return render(request,"sports/chennaisports.html",{'sport1':sport1,'sport2':sport2,'sport3':sport3,'sport4':sport4})
def thanjavursports(request):
    sport1=Sport1.objects.filter(status=0)
    sport2=Sport2.objects.filter(status=0)
    sport3=Sport3.objects.filter(status=0)
    sport4=Sport4.objects.filter(status=0)
    return render(request,"sports/chennaisports.html",{'sport1':sport1,'sport2':sport2,'sport3':sport3,'sport4':sport4})
def coimbatoresports(request):
    sport1=Sport1.objects.filter(status=0)
    sport2=Sport2.objects.filter(status=0)
    sport3=Sport3.objects.filter(status=0)
    sport4=Sport4.objects.filter(status=0)
    return render(request,"sports/chennaisports.html",{'sport1':sport1,'sport2':sport2,'sport3':sport3,'sport4':sport4})
def tirichysports(request):
    sport1=Sport1.objects.filter(status=0)
    sport2=Sport2.objects.filter(status=0)
    sport3=Sport3.objects.filter(status=0)
    sport4=Sport4.objects.filter(status=0)
    return render(request,"sports/chennaisports.html",{'sport1':sport1,'sport2':sport2,'sport3':sport3,'sport4':sport4})
def chennaileo(request,cname,mname):
    if(Movie_collections.objects.filter(name=cname,status=0)):
        if(Movies.objects.filter(Movie_name=mname,status=0)):
            movies=Movies.objects.filter(Movie_name=mname,status=0)
            return render(request,'chennai/chennaileo.html',{'movies':movies})
        else:
            messages.error(request,"No such movie found")
            return render(request,'home.html')
    else:
        messages.error(request,"No such movie found")
        return render(request,'home.html')
    
    
def chennaieswaran(request):
    return render(request,"chennai/chennaieswaran.html")  
def chennaipichai(request):
    return render(request,"chennai/chennaipichai.html") 
def chennaithunivu(request):
    return render(request,"chennai/chennaithunivu.html") 
def chennaihridhayam(request):
    return render(request,"chennai/chennaihridhayam.html") 
def chennaiwhatif(request,cname,mname):
    if(Streaming_collections.objects.filter(name=cname,status=0)):
        if(Stream.objects.filter(Stream_name=mname,status=0)):
            streams=Stream.objects.filter(Stream_name=mname,status=0)
            return render(request,'chennai/chennaiwhatif.html',{'streams':streams})
        else:
            messages.error(request,"No such movie found")
            return render(request,'home.html')
    else:
        messages.error(request,"No such movie found")
        return render(request,'home.html')
    
def chennaifamilyman(request):
    return render(request,"chennai/chennaifamilyman.html")  
def chennaidaddy(request):
    return render(request,"chennai/chennaidaddy.html") 
def chennaicompany(request):
    return render(request,"chennai/chennaicompany.html")  
def chennaikaduva(request):
    return render(request,"chennai/chennaikaduva.html") 
def chennai118(request):
    return render(request,"chennai/chennai118.html")
def chennaiar(request,cname,mname):
    if(Event_collections.objects.filter(name=cname,status=0)):
        if(Events.objects.filter(Events_name=mname,status=0)):
            events=Events.objects.filter(Events_name=mname,status=0)
            return render(request,'chennai/chennaiar.html',{'events':events})
        else:
            messages.error(request,"No such movie found")
            return render(request,'home.html')
    else:
        messages.error(request,"No such movie found")
        return render(request,'home.html')
def chennaihari(request):
    return render(request,"chennai/chennaihari.html")  
def chennaishreya(request):
    return render(request,"chennai/chennaishreya.html")  
def chennaiarjith(request):
    return render(request,"chennai/chennaiarjith.html")  
def chennaimarathon(request,cname,mname):
    if(Sports_collections.objects.filter(name=cname,status=0)):
        if(Sports.objects.filter(Sports_name=mname,status=0)):
            sports=Sports.objects.filter(Sports_name=mname,status=0)
            return render(request,'chennai/chennaimarathon.html',{'sports':sports})
        else:
            messages.error(request,"No such movie found")
            return render(request,'home.html')
    else:
        messages.error(request,"No such movie found")
        return render(request,'home.html')
def chennaisoccer(request):
    return render(request,"chennai/chennaisoccer.html")
def chennaitennis(request):
    return render(request,"chennai/chennaitennis.html")
def chennaicricket(request):
    return render(request,"chennai/chennaicricket.html")  
def maduraimaamannan(request):
    return render(request,"madurai/maduraimaamannan.html")  
def maduraiaram(request):
    return render(request,"madurai/maduraiaram.html") 
def maduraileo(request):
    return render(request,"madurai/maduraileo.html") 
def maduraimanadu(request):
    return render(request,"madurai/maduraimanadu.html") 
def chennaitheatre(request,jname):
    if(Movies.objects.filter(Movie_name=jname,status=0)):
        theatre=Movies.objects.filter(Movie_name=jname,status=0)
        return render(request,"theatre/chennaileotheatre.html",{'theatre':theatre})
def chennaihritheatre(request):
    return render(request,"theatre/chennaihritheatre.html")
def chennaipichaitheatre(request):
    return render(request,"theatre/chennaipichaitheatre.html")
def chennaithunitheatre(request):
    return render(request,"theatre/chennaithubitheatre.html")
def theatrechennaiags(request):
    return render(request,"theatrechennai/theatrechennaiags.html")
def theatrechennaianna(request):
    return render(request,"theatrechennai/theatrechennaianna.html")
def theatrechennaitnagar(request):
    return render(request,"theatrechennai/theatrechennaitnagar.html")
def theatrechennaianandh(request):
    return render(request,"theatrechennai/theatrechennaianandh.html")
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"register.html",{'form': form})

        

