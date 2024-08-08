"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ),
    path('logout/',views.log_out),
    path('kanyakumari/',views.kanyakumari),
    path('madurai/',views.madurai),
    path('thanjavur/',views.thanjavur),
    path('coimbatore/',views.coimbatore),
    path('tirichy/',views.tirichy),
    path('chennaimovies/',views.chennaimovies),
    path('maduraimovies/',views.maduraimovies),
    path('kumarimovies/',views.kumarimovies),
    path('thanjavurmovies/',views.thanjavurmovies),
    path('coimbatoremovies/',views.coimbatoremovies),
    path('tirichymovies/',views.tirichymovies),
    path('chennaistreaming/',views.chennaistreaming),
    path('maduraistreaming/',views.maduraistreaming),
    path('kumaristreaming/',views.kumaristreaming),
    path('thanjavurstreaming/',views.thanjavurstreaming),
    path('coimbatorestreaming/',views.coimbatorestreaming),
    path('tirichystreaming/',views.tirichystreaming),
    path('chennaievents/',views.chennaievents),
    path('maduraievents/',views.maduraievents),
    path('kumarievents/',views.kumarievents),
    path('thanjavurevents/',views.thanjavurevents),
    path('coimbatoreevents/',views.coimbatoreevents),
    path('tirichyevents/',views.tirichyevents),
    path('chennaisports/',views.chennaisports),
    path('maduraisports/',views.maduraisports),
    path('kumarisports/',views.kumarisports),
    path('thanjavursports/',views.thanjavursports),
    path('coimbatoresports/',views.coimbatoresports),
    path('tirichysports/',views.tirichysports),
    path('<str:cname>/<str:mname>/',views.chennaileo),
    path('chennaieswaran/',views.chennaieswaran),
    path('chennaipichai/',views.chennaipichai),
    path('chennaithunivu/',views.chennaithunivu),
    path('chennaihridhayam/',views.chennaihridhayam),
    path('chennai118/',views.chennai118),
    path('streams/<str:cname>/<str:mname>/',views.chennaiwhatif),
    path('chennaifamilyman/',views.chennaifamilyman),
    path('chennaidaddy/',views.chennaidaddy),
    path('chennaicompany/',views.chennaicompany),
    path('chennaikaduva/',views.chennaikaduva),
    path('event/<str:cname>/<str:mname>/',views.chennaiar),
    path('chennaihari/',views.chennaihari),
    path('chennaiarjith/',views.chennaiarjith),
    path('chennaishreya/',views.chennaishreya),
    path('sports/<str:cname>/<str:mname>/',views.chennaimarathon),
    path('chennaisoccer/',views.chennaisoccer),
    path('chennaitennis/',views.chennaitennis),
    path('chennaicricket/',views.chennaicricket),
    path('maduraimaamannan/',views.maduraimaamannan),
    path('maduraiaram/',views.maduraiaram),
    path('maduraileo/',views.maduraileo),
    path('maduraimanadu/',views.maduraimanadu),
    path('<str:jname>/',views.chennaitheatre),
    path('chennaihritheatre/',views.chennaihritheatre),
    path('chennaipichaitheatre/',views.chennaipichaitheatre),
    path('chennaithunitheatre/',views.chennaithunitheatre),
    path('theatre/chennai/ags/',views.theatrechennaiags),
    path('theatre/chennai/anna/',views.theatrechennaianna),
    path('theatre/chennai/tnagar/',views.theatrechennaitnagar),
    path('theatre/chennai/nandh/',views.theatrechennaianandh),
    path('regbi/registration/register',views.register),
    
]    

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)