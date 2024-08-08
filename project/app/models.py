from django.db import models
from django.contrib.auth.models import User
from django.db import models
import datetime
import os
  
  
def getFilename(request,filename):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Movie_collections(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    Movie_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

    
class Streaming_collections(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    Streaming_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Event_collections(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    Event_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Sports_collections(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    Sport_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Chennai_Tamil_movies(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    movie_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Chennai_Other_movies(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    movie_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Chennai_Other1_movies(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    movie_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Chennai_Cartoon_movies(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    movie_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Streaming1(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    stream_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Streaming2(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    stream_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Streaming3(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    stream_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Streaming4(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    stream_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Event1(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    event_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Event2(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    event_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Event3(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    event_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Event4(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    event_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Sport1(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    sport_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Sport2(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    sport_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Sport3(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    sport_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Sport4(models.Model):
    name=models.CharField(max_length=150,null=False, blank=False)
    image=models.ImageField(upload_to=getFilename)
    sport_name=models.CharField(max_length=150)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Movies(models.Model):
    Category=models.ForeignKey(Movie_collections,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=getFilename,null=False,blank=False)
    Movie_name=models.CharField(max_length=150,null=False,blank=False)
    Quality=models.CharField(max_length=150)
    Languages=models.CharField(max_length=150)
    Concept=models.CharField(max_length=1000)
    Cast1=models.ImageField(upload_to=getFilename)
    Cast1_name=models.CharField(max_length=100)
    Cast2=models.ImageField(upload_to=getFilename)
    Cast2_name=models.CharField(max_length=100)
    Cast3=models.ImageField(upload_to=getFilename)
    Cast3_name=models.CharField(max_length=100)
    Cast4=models.ImageField(upload_to=getFilename)
    Cast4_name=models.CharField(max_length=100)
    Crew1=models.ImageField(upload_to=getFilename)
    Crew1_name=models.CharField(max_length=100)
    Crew2=models.ImageField(upload_to=getFilename)
    Crew2_name=models.CharField(max_length=100)
    Crew3=models.ImageField(upload_to=getFilename)
    Crew3_name=models.CharField(max_length=100)
    Crew4=models.ImageField(upload_to=getFilename)
    Crew4_name=models.CharField(max_length=100)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Movie_name
class Stream(models.Model):
    Category=models.ForeignKey(Streaming_collections,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=getFilename,null=False,blank=False)
    Stream_name=models.CharField(max_length=150,null=False,blank=False)
    Quality=models.CharField(max_length=150)
    Languages=models.CharField(max_length=150)
    Concept=models.CharField(max_length=1000)
    Amount=models.CharField(max_length=100)
    Cast1=models.ImageField(upload_to=getFilename)
    Cast1_name=models.CharField(max_length=100)
    Cast2=models.ImageField(upload_to=getFilename)
    Cast2_name=models.CharField(max_length=100)
    Cast3=models.ImageField(upload_to=getFilename)
    Cast3_name=models.CharField(max_length=100)
    Cast4=models.ImageField(upload_to=getFilename)
    Cast4_name=models.CharField(max_length=100)
    Crew1=models.ImageField(upload_to=getFilename)
    Crew1_name=models.CharField(max_length=100)
    Crew2=models.ImageField(upload_to=getFilename)
    Crew2_name=models.CharField(max_length=100)
    Crew3=models.ImageField(upload_to=getFilename)
    Crew3_name=models.CharField(max_length=100)
    Crew4=models.ImageField(upload_to=getFilename)
    Crew4_name=models.CharField(max_length=100)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Stream_name
class Sports(models.Model):
    Category=models.ForeignKey(Sports_collections,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=getFilename,null=False,blank=False)
    Sports_name=models.CharField(max_length=150,null=False,blank=False)
    Date_and_time=models.CharField(max_length=150)
    Place=models.CharField(max_length=150)
    Amount=models.CharField(max_length=100)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Sports_name
class Events(models.Model):
    Category=models.ForeignKey(Event_collections,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=getFilename,null=False,blank=False)
    Events_name=models.CharField(max_length=150,null=False,blank=False)
    Date_and_time=models.CharField(max_length=150)
    Place=models.CharField(max_length=150)
    Amount=models.CharField(max_length=100)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Events_name

class details(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)   
     seat=models.IntegerField(null=False,blank=False);
     amount=models.IntegerField(null=False,blank=False);
