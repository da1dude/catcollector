from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #this is our route for the index page of cats
    path('cats/', views.cats_index, name='index'),
    #route for the detail page of our cats
    #we need an id as well as a way to refer to the id(a route paramater)
    path('cats/<int:cat_id>', views.cats_detail, name='detail')
]