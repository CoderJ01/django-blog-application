from django.urls import path # default django function that allows urls to be configured
from . import views

urlpatterns = [
    path('', views.index, name='index'), # blank means the default url of the website
                                         # when user comes to the website, the views.index function will be triggered
    path('post', views.post, name='post') # add /post url to site
]