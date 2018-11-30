"""kridathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include

from . import views

from mini_project.views import FAQ
from mini_project.views import about
from mini_project.views import game
from mini_project.views import event
from mini_project.views import tournament
from mini_project.views import athletics
from mini_project.views import badminton
from mini_project.views import basketball
from mini_project.views import chess
from mini_project.views import cricket
from mini_project.views import football
from mini_project.views import handball
from mini_project.views import volleyball
from mini_project.views import hockey


urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.FAQ, name='FAQ'),
    url(r'^FAQ/$', FAQ),
    url(r'^about/$', about),
    url(r'^game/$', game),
    url(r'^event/$', event),  
    url(r'^game/tournament/$', tournament),
    url(r'^game/athletics/$', athletics),
    url(r'^game/badminton/$', badminton),
    url(r'^game/basketball/$', basketball),
    url(r'^game/chess/$', chess),
    url(r'^game/cricket/$', cricket),
    url(r'^game/football/$', football),
    url(r'^game/handball/$', handball),
    url(r'^game/volleyball/$', volleyball),
    url(r'^game/hockey/$', hockey),
    
] 


"""
from django.conf.urls import url, include

from index import views


urlpatterns = [
    
    url(r'^index/', views.index),
    url(r'^FAQ', views.FAQ),
]
"""